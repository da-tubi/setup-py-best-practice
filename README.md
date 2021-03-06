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

In this repo, we find the next version and the set it to the environment variable `SETUPTOOLS_SCM_PRETEND_VERSION`. With `SETUPTOOLS_SCM_PRETEND_VERSION` provided, `make version` and we will find that the manually assigned one will override the automatically derived version.

## Best Practice 4: `__version__`
Since Python 3.8, we could use the following code snippet to provide `__version__`.

``` python
from importlib.metadata import version

__version__ = version('setup-py-best-practice')
```

Here is how we test it:
``` bash
$ make install
pip install -e .
Installing collected packages: setup-py-best-practice
  Running setup.py develop for setup-py-best-practice
Successfully installed setup-py-best-practice-0.0.2.dev3+ga93e31a.d20220615
```
``` bash
$ python
Python 3.8.10 (default, May 19 2021, 11:01:55)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import demo
>>> demo.__version__
'0.0.2.dev3+ga93e31a.d20220615'
>>>
```

## Best Practice 5: Cache Python dependencies in Test CI by [@Renkai](https://github.com/Renkai)
In this demo repo, there is only one direct dependency `pytest`.

| Attempt | Cache Hit | elapsed time of pip install | total elapsed time |
|---------|-----------|-----------------------------|--------------------|
| 1       | No        | 5s                          | 13s                |
| 2       | Yes       | 3s                          | 9s                 |
| 3       | Yes       | 2s                          | 11s                |

For more info: [How can I use pip cache in github actions](https://stackoverflow.com/a/70638014)

