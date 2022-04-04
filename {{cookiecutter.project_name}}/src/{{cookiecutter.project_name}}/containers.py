import logging.config
from pathlib import Path

import yaml
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer


def _get_path(file: str) -> Path:
    return Path(__file__).resolve().parent / file


def _init_logging():
    with open(_get_path("logging.yml"), "r") as f:
        logging.config.dictConfig(yaml.safe_load(f.read()))


class Container(DeclarativeContainer):
    configure_logging = providers.Resource(_init_logging)
    config = providers.Configuration()
    config.from_yaml(_get_path("config.yml"), required=True)  # noqa: CCE002
