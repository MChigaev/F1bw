# -*- coding: utf-8 -*-
#
# Copyright (C) 2018, Michael Chigaev.
#
# F1bw is free software; you can redistribute it and/or modify
# it under the terms of the 3-Clause BSD License; see LICENSE.txt
# file for more details.
#
#
# Developers, install with:
#    pip install -r requirements.txt
#    python setup.py develop
#
from distutils.cmd import Command
import distutils.log as logger
from os import environ as environ
import platform
import shutil
import string
import subprocess # noqa
import sys
from setuptools import setup, find_packages
from setuptools.command import build_py, develop, install
# Version restrictions and dependencies
if sys.version_info < (3, 4, 0, 'final', 0):
    raise SystemExit("This package requires python 3.4 or higher.")
elif sys.version_info >= (3, 6, 0, 'final', 0):
    pass
else:
    pass
from pathlib import Path  # python 3.4

NAME = 'F1bw'
C_NAME = 'F1bw'
C_VERSION = '0.0.1'
BINARY_NAME = C_NAME + '-' + NAME
ENV_SCRIPT_INNAME = 'server_env.sh'
ENV_SCRIPT_OUTNAME = NAME + '_env'
RUN_SCRIPT_INNAME = 'server_run.py'
RUN_SCRIPT_OUTNAME = NAME + '_run.py'
SOURCE_PATH = Path('.') / NAME / C_NAME.lower() + ".py"
BUILD_PATH = Path('.') / NAME / 'bin'
DIR_MODE = 0o775

#
# Most of the setup function has been moved to setup.cfg,
# which requires a recent setuptools to work.  Current
# anaconda setuptools is too old, so it is strongly
# urged this package be installed in a virtual environment.
#

tests_require = [
    #'check-manifest>=0.25',
    #'coverage>=4.0',
    #'isort>=4.2.2.2',
    #'pydocstyle>=1.0.0',
    #'pytest-cache>=1.0',
    #'pytest-cov>=1.8.0',
    #'pytest-pep8>=1.0.6',
    #'pytest>=2.8.0'
]

extras_require = dict(docs=['Sphinx>=1.4.2'], tests=tests_require)

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

packages = find_packages()

setup(
    description=__doc__,
    packages=packages,
    setup_requires=['packaging',
                    'setuptools>30.3.0',
                    'setuptools-scm>1.5'
                    ],
    entry_points={
        'console_scripts': [NAME + ' = ' + NAME + '.cli:cli']
    },
    cmdclass={
        #'build_cbinary': BuildCBinaryCommand,
        #'build_py': BuildPyCommand,
        #'develop': DevelopCommand,
        #'install_binaries': InstallBinariesCommand,
        #'install': InstallCommand
    },
    use_scm_version={
        'version_scheme': 'guess-next-dev',
        'local_scheme': 'dirty-tag',
        'write_to': NAME + '/version.py'
    },
    extras_require=extras_require,
    tests_require=tests_require,
)
