import os
import re
import sys

from setuptools import find_packages, setup

setup(
    name="paramara",
    version="0.1",
    packages=find_packages(),
    author="Mustafa Atik",
    author_email="muatik@gmail.com",
    long_description=open('README.md').read(),
    description='stock price crawler',
    license="MIT",
    url="https://github.com/muatik/paramara",
    platforms=['any'],
)
