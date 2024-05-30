from setuptools import find_packages, setup
from typing import List




setup(
    name = 'sensor',
    version = '0.0.1',
    author = "amogh",
    author_email = "amogh9792@gmail.com",
    packages = find_packages(),
    install_requires = ["pymongo"]
)