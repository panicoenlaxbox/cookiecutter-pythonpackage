import os
import re

import toml
from setuptools import find_packages, setup


def get_version():
    pattern = r"VERSION\s*=\s*\((?P<version>\d+,\s*\d+,\s*\d+)\)"
    with open(os.path.join("{{cookiecutter.project_name}}", "version.py")) as f:
        content = f.read()
        match = re.search(pattern, content, re.RegexFlag.IGNORECASE | re.RegexFlag.MULTILINE)
        version = match["version"].replace(",", ".").replace(" ", "")

    if os.environ.get("VERSION_SUFFIX") is not None:
        version += f"{version}.{os.environ['VERSION_SUFFIX']}"

    return version


def get_long_description():
    with open("README.md") as file:
        return file.read()


def get_install_requires():
    if os.path.isfile("requirements.txt"):
        pattern = r"(.+==.+?)(;{1}|\s)"
        with open("requirements.txt") as f:
            content = f.read()
            return [
                match[0] for match in re.findall(pattern, content, re.RegexFlag.IGNORECASE | re.RegexFlag.MULTILINE)
            ]
    else:
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
