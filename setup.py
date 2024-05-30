from setuptools import find_packages, setup
from typing import List

def get_requirements() -> list[str]:
    """
    This function will return list of requirements
    """

    requirements_list : list[str] = []

    return requirements_list


setup(
    name = 'sensor',
    version = '0.0.1',
    author = "amogh",
    author_email = "amogh9792@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)