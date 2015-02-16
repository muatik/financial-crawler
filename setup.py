import os
import re
import sys

from setuptools import find_packages, setup

long_description = """
This is an experimental work about detectiong correlations and causations
in stock prices by looking at stock prices, commodities, currencies etc...
"""

setup(
    name="paramara",
    version="0.1",
    packages=find_packages(),
    author="Mustafa Atik",
    author_email="muatik@gmail.com",
    long_description=long_description,
    description='stock price crawler',
    license="MIT",
    url="https://github.com/muatik/paramara",
    platforms=['any'],
)
