#!/usr/bin/env python3
# -*- mode: python -*-
# -*- coding: utf-8 -*-
#

"""
setuptools/pip installer for swagger-python-codegen.
"""

from pathlib import Path
from setuptools import (setup, find_packages)

# noinspection PyPackageRequirements,PyUnresolvedReferences
import swagger_python_codegen

THISDIR = Path(__file__).resolve().parent

setup(
    name='swagger_python_codegen',
    version=swagger_python_codegen.__version__,
    description="Swagger API SDK code generator for Python",
    url="https://github.comcast.com/ea/ea_resource_manager_api",
    author="VIPER End-To-End Test (VET) Platform Automation (PA) Team",
    author_email='momus@comcast.com',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generator",
        "Topic :: Software Development :: RESTful API",
        "Topic :: Software Development :: RESTful SDK",
    ],
    packages=find_packages(),
    install_requires=Path(THISDIR, 'requirements.txt').read_text(encoding='utf-8'),
    keywords="rest restful api flask swagger openapi generator",
    scripts=['bin/swagger-python-codegen'],
)
