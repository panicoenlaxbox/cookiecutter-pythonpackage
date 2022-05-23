import logging.config

import yaml
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer


def _logging_resource():
    with open("logging.yml", "r") as f:
        logging.config.dictConfig(yaml.safe_load(f.read()))


class Container(DeclarativeContainer):
    _logging_resource = providers.Resource(_logging_resource)
    config = providers.Configuration()
    config.from_yaml("config.yml", required=True)  # noqa: CCE002
