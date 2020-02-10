UniMorph canonicalization
=========================

**🚧 work in progress 👷**

This directory contains code for canonicalizing and validating
[UniMorph](https://unimorph.github.io/) feature bundles according to the
[official
documentation](www.unimorph.org/doc/Sylak-Glassman_2016_-_UniMorph_Schema_User_Guide.pdf).
The included command-line tool `um_canonicalize` converts UniMorph files
(three-column TSV files consisting of lemma, inflection, and feature bundle) so
that the features are placed in a canonical order (see below). This tool is
written in Pure Python and has no external dependencies except setuptools and
YAML.

Command-line tool
-----------------

### Installation

This package requires Python 3.6+.

You can install the package from GitHub directly using the following command:

``` {.bash}
pip install git+https://github.com/unimorph/um-canonicalize.git
```

### Usage

After installation, the terminal command `um_canonicalize` will be available.
For instance, if you have the modern Greek UniMorph file `ell` in your working
directory, you can issue:

``` {.bash}
um_canonicalize ell
```

This should enforce the canonicalization (described below) on the file, failing
if any conflicts or inconsistencies are detected; running this tool on its own
(successful) output should print "0 feature bundles canonicalized".

Canonical order
---------------

We propose a canonical ordering of tags within a feature bundle as follows.

-   The first tag is the "Part of Speech" tag.
-   The remaining universal tags are then placed in lexicographic order of the
    category they represent; e.g., `SEMEL` ("semelfactive"), an Aktsionsart
    feature, comes before `ANIM` ("animate").
-   Any language-specific (e.g., `LGSPEC`) tags are then placed at the end, in
    their lexicographic order.

This ordering is enforced by [`um-canonicalize`](um-canonicalize.py)\`; running
this tool on its own output should print "0 feature bundles canonicalized" to
STDERR.

See [`CHANGES.md`](changes.md) for changes to the schema since UniMorph 2.0.

Contributing
------------

The list of features in [`tags.yaml`](tags.yaml) has some known gaps. See
[`CONTRIBUTING.md`](contributing.md) for information about how to submit
improvements to this file.

Author
------

These tools were created by [Kyle Gorman](mailto:kylebgorman@gmail.com).
