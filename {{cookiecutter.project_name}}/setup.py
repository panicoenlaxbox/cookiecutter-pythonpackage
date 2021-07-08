import os
import re

import toml
from setuptools import find_packages, setup


def get_name():
    name = "{{cookiecutter.project_name}}"
    {%- if cookiecutter.packaging_strategy == 'branch' %}
    if os.environ.get("PACKAGE_SUFFIX") is not None:
        name = f"{name}-{os.environ['PACKAGE_SUFFIX']}"
    {%- endif %}
    return name


def get_version():
    pattern = r"VERSION\s*=\s*\((?P<version>\d+,\s*\d+,\s*\d+)\)"
    with open(os.path.join("{{cookiecutter.project_name}}", "version.py")) as f:
        content = f.read()
        match = re.search(pattern, content, re.RegexFlag.IGNORECASE | re.RegexFlag.MULTILINE)
        version = match["version"].replace(",", ".").replace(" ", "")
    {%- if cookiecutter.packaging_strategy == '440' %}
    if os.environ.get("VERSION_SUFFIX") is not None:
        version += f"{version}.{os.environ['VERSION_SUFFIX']}"
    {%- endif %}
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
packages = find_packages(
    exclude=["tests", "tests.*"]
)  # https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html#using-find-or-find-

setup(
    name=get_name(),
    version=get_version(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=packages,
    install_requires=install_requires,
    include_package_data=True,  # https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
    package_data={"": ["*.json", "py.typed"]},  # https://www.python.org/dev/peps/pep-0561/
)
