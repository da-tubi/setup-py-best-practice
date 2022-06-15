#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import pathlib

with open(
    pathlib.Path(__file__).absolute().parent / "README.md", "r"
) as fh:
    long_description = fh.read()

setup(
    url='https://github.com/da-tubi/setup-py-best-practice',
    name='setup-py-best-practice',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Darcy Shen',
    author_email='sadhen@zoho.com.cn',
    description='A demo project to show the best practice of setup.py',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['demo'],
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='setuptools best practice',
)
