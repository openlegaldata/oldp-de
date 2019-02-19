#!/usr/bin/env python

from __future__ import print_function

import codecs
import os
import re

from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='oldp_de',
    version=find_version('oldp_de', '__init__.py'),
    url='https://github.com/openlegaldata/oldp-de',
    license='MIT',
    description='German Theme for Open Legal Data Platform',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Malte Schwarzer',
    author_email='hello@openlegaldata.io',
    packages=find_packages(),
    install_requires=[
        # Packages 
        # ...
    ],
    dependency_links=[
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)

