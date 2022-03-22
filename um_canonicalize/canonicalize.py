"""Canonicalizes feature vectors in UniMorph TSV files.

This applies a number of basic transformations (in particular, sorting) to the
feature vector column of UniMorph TSV files.

For additional context see the original UniMorph schema guidelines:

    www.unimorph.org/doc/Sylak-Glassman_2016_-_UniMorph_Schema_User_Guide.pdf

But note that this supersedes said document as of UniMorph 3.0.
"""

__author__ = "Kyle Gorman"


import argparse
import csv
import logging
import pkg_resources
import re
import sys

from typing import Dict

import yaml

# This maps each feature onto a position in the feature order. By retrieving
# these for each feature we can sort (or detect inconsistencies).
#
# We use the following tag ordering conventions:
#
# -   The first tag is the part of speech tag.
# -   The remaining universal tags are then placed in lexicographic order of
#     the category they represent; e.g., `SEMEL` ("semelfactive"), an
#     Aktionsart feature, comes before `ANIM` ("animate"), an animcy feature.
# -   Any language-specific (e.g., `LGSPEC`) tags are then placed at the end,
#     in their lexicographic order.
#
# Therefore the indices here are ascending except for part of speech (for which
# we reserve 0) and language-specific features (which we handle using a regular
# expression).
#
# TODO(feature): Deal with locative case combinations like `IN+ESS`.
# TODO(feature): Deal with the CN_R_MN switch-reference schemata.

LGSPEC = r"LGSPEC(\d{1,})$"

# Added to the integer in LGSPEC, this gives us its index.
LGSPEC_START = 24


def _load_table(path: str) -> Dict[str, int]:
    with open(path, "r") as source:
        spec = yaml.safe_load(source)
    cat_to_index = {cat: i for (i, cat) in enumerate(spec["ordering"])}
    table: Dict[str, int] = {}
    for (cat, tags) in spec["categories"].items():
        index = cat_to_index[cat]
        for tag in tags:
            table[tag] = index
    return table


def main() -> None:
    logging.basicConfig(level="INFO", format="%(levelname)s: %(message)s")
    parser = argparse.ArgumentParser(
        description="Canonicalizes feature vectors in UniMorph TSV files"
    )
    parser.add_argument("input_path")
    args = parser.parse_args()

    table = _load_table(pkg_resources.resource_filename(__name__, "tags.yaml"))

    # This keeps track of how many bundles were rewritten. If run twice
    # the second time the answer should be 0.
    canonicalized = 0

    with open(args.input_path, "r") as source:
        # TODO: these files contain a bunch of blank lines. Probably should
        # strip them out ahead of time but alternatively we could complexify
        # things here.
        tsv_reader = csv.reader(source, delimiter="\t")
        tsv_writer = csv.writer(sys.stdout, delimiter="\t")
        for (n, (lemma, inflection, features_str)) in enumerate(tsv_reader, 1):
            features = features_str.split(";")
            assert features, "Empty feature vector"
            # Keys are natural number indices; values are the features for
            # that slot.
            slots: Dict[int, str] = {}
            for feature in features:
                try:
                    index = table[feature]
                except KeyError:
                    mtc = re.match(LGSPEC, feature)
                    if mtc:
                        index = LGSPEC_START + int(mtc.group(1))
                    else:
                        logging.error(
                            "Unknown feature: %r (file %s, line %d)",
                            feature,
                            args.input_path,
                            n,
                        )
                        exit(1)
                current = slots.get(index)
                if current:
                    logging.error(
                        "Feature conflict: %r and %r (file %s, line %d)",
                        current,
                        feature,
                        args.input_path,
                        n,
                    )
                    exit(1)
                slots[index] = feature
            canonicalized_features = [
                value for (_, value) in sorted(slots.items())
            ]
            if canonicalized_features != features:
                features_str = ";".join(canonicalized_features)
                canonicalized += 1
            tsv_writer.writerow((lemma, inflection, features_str))

    logging.info("%d feature bundles canonicalized", canonicalized)


if __name__ == "__main__":
    main()
