[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![ci](https://github.com/your_organization/your_repository/actions/workflows/ci.yml/badge.svg)
![cd](https://github.com/your_organization/your_repository/actions/workflows/cd.yml/badge.svg)

# Installation

```powershell
$env:AZURE_DEVOPS_PAT="YOUR_PAT"  # Only needed once for the following command
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

## AZURE_DEVOPS_PAT

This environment variable is used by Pipenv to download packages from a private feed.

During the project generation, it's written in `.env` file that it's excluded from source control in `.gitignore` file.

If you want to change the default location of `.env` file, you can use [PIPENV_DOTENV_LOCATION](https://pipenv.pypa.io/en/latest/advanced/#pipenv.environments.PIPENV_DOTENV_LOCATION)

## PyCharm

When you open PyCharm, in addition to selecting the interpreter created previously in a global manner, you must select it for each Run/Debug configuration.

For pytest, you must go to Settings > Tools > Python Integrated Tools and select pytest like default test runner.

### Environment variables

PyCharm/pipenv have a bug and `.env` files are not loaded in Terminal [Terminal not loading environmental variables with PIPENV](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360001761299-Terminal-not-loading-environmental-variables-with-PIPENV), so you should execute `pipenv shell` in PyCharm Terminal every time you open it.

### Run/Debug configuration

For using `.env` file with a PyCharm Run/Debug configuration, you should install [EnvFile](https://plugins.jetbrains.com/plugin/7861-envfile) plugin and choose the `.env` file in a proper way.

## GitHub Action

### Secrets

You must set the following secrets in the repository:

- `AZURE_DEVOPS_PAT`, a PAT for reading your private feed.
- `TWINE_PASSWORD`, a PAT for writing your private feed.

If you want, both can be the same PAT.

Moreover, although in `ci.yml` and `cd.yml` you will find the python version that you specified during the bootstraping, you should check this version and align it with the existing versions in https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json

### Badges

You must fix in README.md the badge url with the right repository name for properly working the GitHub badges.
