import os
import re
import sys

from setuptools import find_packages, setup

requirements_file = "requirements.txt"
requirements = [pkg.strip() for pkg in open(requirements_file).readlines()]

setup(
    name="parapul",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    author="Mustafa Atik",
    author_email="muatik@gmail.com",
    long_description=open('README.md').read(),
    description='stock price crawler',
    license="MIT",
    url="https://github.com/muatik/paramara",
    platforms=['any'],
)
