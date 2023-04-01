#!/usr/bin/env python3
"""
Pyro Lexer
==========

A Pygments lexer for the Pyro programming language.

"""

import os
import re
import io
from setuptools import setup

filepath = os.path.join(os.path.dirname(__file__), 'pyro_lexer.py')
with io.open(filepath, encoding='utf-8') as metafile:
    regex = r'''^__([a-z]+)__ = ["'](.*)["']'''
    meta = dict(re.findall(regex, metafile.read(), flags=re.MULTILINE))

entry_points = """
[pygments.lexers]
pyro=pyro_lexer:PyroLexer
"""

setup(
    name = 'pyro-lexer',
    version = meta['version'],
    py_modules = ['pyro_lexer'],
    author = 'Darren Mulholland',
    url = 'https://github.com/dmulholl/pyro-lexer',
    license = '0BSD',
    description = "A Pygments lexer for Pyro.",
    long_description = __doc__,
    entry_points=entry_points,
    install_requires=["Pygments>=2.0.1"],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: General',
    ],
)
