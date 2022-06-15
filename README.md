# setup.py best practice
Here are several best practices.

## Best Practice 1: Use Makefile to provide shortcut
+ `make version`: show the current version
+ `make install`: install the current branch for local development

## Best Practice 2: Version for Local Developmenet
``` bash
$ make version
0.0.2.dev2+gaaa0b31
```
`0.0.2` is the next version of the latest git tag `0.0.1`. The `devX` part is automatically generated.

For more info: https://github.com/pypa/setuptools_scm

## Best Practice 3: Github Action to publish it to JFROG/PYPI
Github Action [codacy/git-version](https://github.com/codacy/git-version) is adopted to find the next version (Semver based) of the latest git tag `0.0.1`.

In this repo, we find the next version and the set it to the environment variable `SETUPTOOLS_SCM_PRETEND_VERSION`. With `SETUPTOOLS_SCM_PRETEND_VERSION` provided, `make version` and we will found that the manually assigned one will override the automatically derived version.
