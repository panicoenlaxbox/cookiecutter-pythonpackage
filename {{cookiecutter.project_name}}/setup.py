import re
from os import environ
from pathlib import Path

from setuptools import find_packages, setup


def get_name():
    name = "{{cookiecutter.project_name}}"
    {%- if cookiecutter.packaging_strategy == "branch" %}
    if environ.get("PACKAGE_SUFFIX") is not None:
        name = f"{name}-{environ['PACKAGE_SUFFIX']}"
    {%- endif %}
    return name


def get_version():
    pattern = r"VERSION\s*=\s*\((?P<version>\d+,\s*\d+,\s*\d+)\)"
    with open(Path("src").joinpath("other_project").joinpath("version.py")) as f:
        content = f.read()
        match = re.search(pattern, content, re.RegexFlag.IGNORECASE | re.RegexFlag.MULTILINE)
        version = match["version"].replace(",", ".").replace(" ", "")
    {%- if cookiecutter.packaging_strategy == "pep440" %}
    if environ.get("VERSION_SUFFIX") is not None:
        version += f"{version}.{environ['VERSION_SUFFIX']}"
    {%- endif %}
    return version


def get_long_description():
    with open("README.md") as file:
        return file.read()


def get_install_requires():
    excluded_packages = []
    if Path("requirements.txt").exists():
        print("Using requirements.txt")
        packages = [
            match[0]
            for match in re.findall(
                r"(.+==.+?)(;{1}|\s)",
                Path("requirements.txt").read_text(),
                re.RegexFlag.IGNORECASE | re.RegexFlag.MULTILINE,
            )
        ]
        print(f"{len(packages)} packages found {packages}")
        final_packages = []
        for package in packages:
            append = True
            for excluded_package in excluded_packages:
                if package.startswith(f"{excluded_package}=="):
                    append = False
                    break
            if append:
                final_packages.append(package)
        print(f"{len(final_packages)} final packages {final_packages}")
        return final_packages
    else:
        print("Using Pipfile")
        packages = []
        with (open("Pipfile")) as f:
            packages_section = False
            while line := f.readline():
                line = line.strip()
                if line.startswith("[packages]"):
                    packages_section = True
                    continue
                if line == "[dev-packages]":
                    break
                if packages_section and line:
                    package = line.strip().split(" = ")[0].strip()
                    version = line.strip().split(" = ")[1].strip(' "')
                    packages.append((package, version))

        print(f"{len(packages)} packages found {packages}")
        final_packages = [
            package + (version if version != "*" else "")
            for package, version in packages
            if package not in excluded_packages
        ]
        print(f"{len(final_packages)} final packages {final_packages}")
        return final_packages


long_description = get_long_description()
install_requires = get_install_requires()

setup(
    name=get_name(),
    version=get_version(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    install_requires=install_requires,
    include_package_data=True,  # https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
    package_data={"": ["*.json", "py.typed"]},  # https://www.python.org/dev/peps/pep-0561/
    package_dir={"": "src"},
)
