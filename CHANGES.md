The following featural changes have been made since:

    J. Sylak-Glassman. 2016. The composition and use of the universal morphological feature schema (UniMorph schema). Technical report, Department of Computer Science, Johns Hopkins University.

1.  There are two features denoting "proximate": `PRX` for Person, and `PROX`
    for Case and Deixis. The use of the latter for two categories of feature is
    a problem for automatic canonicalization. Therefore we:

    -   Use `PRX` for Case
    -   Use `PROX` for Deixis
    -   Use `PROXI` for Person

For consistency, we also rename the Person feature `OBV` (obviative) to `OBVI`.

2.  Features with trailing integer do not sort lexicographically if the integer
    is greater than 9, which is the case for both the `BANT*` family of noun
    class features and for the `LGSPEC*` family. Therefore, we pad these two
    families using "%02d" so that they read:

    -   `BANT02` instead of the older `BANT2`
    -   `LGSPEC08` instead of the older `LGSPEC8`

etc.

3.  We add support for multiple feature bundles for "portmanteaux". Each feature
    bundle should be separated using `|` and is processed separately.

**Note that this is not supported yet.**
