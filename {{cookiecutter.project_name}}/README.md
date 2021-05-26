[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![ci](https://github.com/your_organization/your_repository/actions/workflows/ci.yml/badge.svg)
![cd](https://github.com/your_organization/your_repository/actions/workflows/cd.yml/badge.svg)

# Installation

```powershell
$env:AZURE_DEVOPS_PAT="YOUR_PAT"  # Only needed once during the project setup
pipenv install --dev
pipenv shell
git init
pre-commit install
git config --local user.email your@email
git add .
git commit -m "Initial commit"
```

# Usage

```bash
python -m main
pytest
```

# Deploying

You can choose different approaches for publishing the package.

If `setup.py` finds a `requirements.txt`, it will use it for pinning dependencies, otherwise it will use `Pipfile` only will take care about your direct dependencies.

If you use `publish.ps1`, `requirements.txt` will be created prior to run `pipenv run publish` script command. Futhermore, `requirements.txt` is excluded in `.gitignore` because it could contain the token supplied during the project generation, `pipenv lock -r > requirements.txt` will be dump it in the file header.

`publish.ps1` is used in the GitHub Action because I assume that you are developing an application, but if it isn't your case and you want to distribute a package for third parties, may be you shouldn't pin your dependencies and left them opened for easily integration with the consumer application. In this case, feel free to change the call to `publish.ps1` in [cd.yml]({{cookiecutter.project_name}}/.github/cd.yml) for a single call to `pipenv run publish`.

# AZURE_DEVOPS_PAT

This environment variable is used by Pipenv to download packages from a private feed.

During the project generation, it's written in `.env` file that it's excluded from source control in `.gitignore` file.

If you want to change the default location of `.env` file, you can use [PIPENV_DOTENV_LOCATION](https://pipenv.pypa.io/en/latest/advanced/#pipenv.environments.PIPENV_DOTENV_LOCATION)

# PyCharm

## pytest

You must go to Settings > Tools > Python Integrated Tools and select pytest like default test runner.

## Environment variables

PyCharm/pipenv have a bug and `.env` files are not loaded in Terminal [Terminal not loading environmental variables with PIPENV](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360001761299-Terminal-not-loading-environmental-variables-with-PIPENV), so you should execute `pipenv shell` in PyCharm Terminal every time you open it.

## Run/Debug configuration

For using `.env` file with a PyCharm Run/Debug configuration, you should install [EnvFile](https://plugins.jetbrains.com/plugin/7861-envfile) plugin and choose the `.env` file in a proper way.

# GitHub Action

## Secrets

You must set the following secrets in the repository:

- `AZURE_DEVOPS_PAT`, a PAT for reading your private feed.
- `TWINE_PASSWORD`, a PAT for writing your private feed.

If you want, both can be the same PAT.

Moreover, although in `ci.yml` and `cd.yml` you will find the python version that you specified during the bootstraping, you should check it and ensure that it's aligned with available versions in https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json

## Badges

You must fix the badge url in `README.md` with the right repository name for properly displaying.
