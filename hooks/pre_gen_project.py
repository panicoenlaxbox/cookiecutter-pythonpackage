import sys
import re


if '-' in '{{cookiecutter.project_name}}':
    print('ERROR: project_name cannot contain a hyphen.')
    sys.exit(1)

if '_' in '{{cookiecutter.package_name}}':
    print('ERROR: package_name cannot contain an underscore.')
    sys.exit(1)

if not re.match(r"^\d{1}.\d+$", "{{cookiecutter.python_version}}"):
    print('ERROR: python_version it not in the format X.Y')
    sys.exit(1)