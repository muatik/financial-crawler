import os
import re
import sys

from setuptools import find_packages, setup

requirements = [
    "pyquery",
    "arrow"
]

setup(
    name="financialCrawler",
    version="0.1.0.6",
    packages=find_packages(),
    install_requires=requirements,
    author="Mustafa Atik",
    author_email="muatik@gmail.com",
    long_description=open('README.md').read(),
    description='stock price crawler',
    license="MIT",
    url="https://github.com/muatik/financial-crawler",
    platforms=['any'],
)
