#!/usr/bin/env python

from distutils.core import setup

setup(
    name='FuckThisCollapse',
    version='0.1',
    description='Fuck This Collapse game',
    author='Andrew Kesterson',
    author_email='andrew@aklabs.net',
    url='https://github.com/akesterson/FuckThisCollapse',
    packages=['fuckthiscollapse'],
    scripts=['scripts/game.py'],
    install_requires=['pygame']
)
