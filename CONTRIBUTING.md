Contributing
============

Thank you for your interest in contributing to this repository.

This page assumes that you have already created a fork of the `um-canonicalize`
repo under your GitHub account and have the codebase available locally for
development work. If you have followed [these
steps](https://github.com/unimorph/um-canonicalize#development), then you
are all set.

Working on a feature or bug fix
-------------------------------

The development steps below assumes that your local Git repo has a remote
`upstream` link to `unimorph/um-canonicalize`:

``` {.bash}
git remote add upstream https://github.com/unimorph/um-canonicalize.git
```

After this step (which you only have to do once), running `git remote -v` should
show your local Git repo has links to both "origin" (pointing to your fork
`<your-github-username>/um-canonicalize`) and "upstream" (pointing to
`unimorph/um-canonicalize`).

To work on a feature or bug fix, here are the development steps:

1.  Before doing any work, check out the master branch and make sure that your
    local master branch is up-to-date with upstream master:

    ``` {.bash}
    git checkout master
    git pull upstream master
    ```

2.  Create a new branch. This branch is where you will make commits of your
    work. (As best practice, never make commits while on a master branch.
    Running `git branch` tells you which branch you are on.)

    ``` {.bash}
    git checkout -b new-branch-name
    ```

3.  Make as many commits as needed for your work.

4.  When you feel your work is ready for a pull request, push your branch to
    your fork.

    ``` {.bash}
    git push origin new-branch-name
    ```

5.  Go to your fork `https://github.com/<your-github-username>/um-canonicalize`
    and create a pull request off of your branch against the
    `unimorph/um-canonicalize` repo.

Documentation
-------------

-   If relevant, please update the top-level [README](README.md) for your
    changes.
