install:
	pip install -e .[dev]

test:
	pytest

version:
	python setup.py --version

anyversion:
	SETUPTOOLS_SCM_PRETEND_VERSION=1.1.1 python setup.py --version
