#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
setup.py for the Python packager
"""

from setuptools import setup
from codecs import open
from os import path
import os
from decmath import __version__

here = path.abspath(path.dirname(__file__))
readme_path = path.join(here, 'README.rst')
with open(readme_path, encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DecMath',
    version=__version__,
    description='The standard math library in Decimal and some extras...',
    long_description=long_description,
    url='https://github.com/ElecProg/decmath',
    author='Evert Provoost',
    author_email='evert.provoost@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords='math Decimal',
    python_requires='>=3',
    packages=['decmath']
)
