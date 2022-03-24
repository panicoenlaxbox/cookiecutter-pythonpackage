{% if cookiecutter.dependency_injector == "y" -%}
import logging
from typing import Any, Dict

from dependency_injector.wiring import Provide, inject

from {{cookiecutter.project_name}}.containers import Container


@inject
def main(config: Dict[str, Any] = Provide[Container.config]) -> None:
    print("Hello {{cookiecutter.project_name}}!")
    logging.info(config)


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    container.init_resources()
    main()
    container.shutdown_resources()
{% else -%}
def main():
    print("Hello {{cookiecutter.project_name}}!")


if __name__ == "__main__":
    main()
{% endif %}