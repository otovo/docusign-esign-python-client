import os

from setuptools import setup, find_packages, Command

NAME = "docusign-esign"
VERSION = "3.15.0"
REQUIRES = [
    "urllib3 >= 1.15",
    "six >= 1.8.0",
    "certifi >= 14.05.14",
    "python-dateutil >= 2.5.3",
    "setuptools >= 21.0.0",
    "PyJWT>=2<3",
    "cryptography>=2.5",
    "nose>=1.3.7"
]


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="DocuSign REST API",
    author_email="devcenter@docusign.com",
    url="",
    keywords=["Swagger", "DocuSign REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    cmdclass={'clean': CleanCommand},
    long_description=long_description,
    long_description_content_type='text/markdown'
)
