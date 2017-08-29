# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "docusign_esign"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "jwcrypto >= 0.4.2"]

setup(
    name=NAME,
    version=VERSION,
    description="DocuSign REST API",
    author_email="",
    url="",
    keywords=["Swagger", "DocuSign REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.
    """
)
