#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

"""if sys.version_info.major == 3:
    requirements = [
        "bsddb3>=5.2.0",
        "pycrypto>=2.5"
    ]
else:
    requirements = []"""

requirements = [
    "bsddb3>=5.2.0",
    "pycrypto>=2.5"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='federated_monsters',
    version='0.4.0',
    description='Federated Monsters is a game that seeks to follow the format of games like Pokemon, but to instead use a federated server format to store and trade creatures',
    long_description=readme + '\n\n' + history,
    author='Colin Atkinson',
    author_email='114d71d1@opayq.com',
    url='https://github.com/colatkinson/federated_monsters',
    packages=[
        'federated_monsters',
    ],
    package_dir={'federated_monsters':
                 'federated_monsters'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='federated_monsters',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
