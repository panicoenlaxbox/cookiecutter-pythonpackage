import os

import toml
from setuptools import find_packages, setup

from {{cookiecutter.project_name}} import __version__


def get_version():
    version = __version__

    if os.environ.get("VERSION_SUFFIX") is not None:
        version = f"{version}.{os.environ['VERSION_SUFFIX']}"

    return version


def get_long_description():
    with open("README.md") as file:
        return file.read()


def get_install_requires():
    data = toml.load("Pipfile")
    return [package + (version if version != "*" else "") for package, version in data["packages"].items()]


long_description = get_long_description()
install_requires = get_install_requires()

setup(
    name="{{cookiecutter.package_name}}",
    version=get_version(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,  # https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
    package_data={"": ["*.json"]},
)
