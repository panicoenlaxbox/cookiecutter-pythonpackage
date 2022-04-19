{% if cookiecutter.pyspark_version -%}
from distutils.dir_util import copy_tree
from pathlib import Path
from typing import Optional

import pytest
from _pytest.fixtures import FixtureRequest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark(request: FixtureRequest):
    spark_: Optional[SparkSession] = None

    request.addfinalizer(lambda: spark_.sparkContext.stop() if spark_ is not None else None)

    def _():
        nonlocal spark_
        if spark_ is not None:
            return spark_
        spark_ = SparkSession.builder.getOrCreate()
        return spark_

    return _


@pytest.fixture()
def test_name(request: FixtureRequest) -> str:
    return request.node.name


@pytest.fixture()
def test_shared_dir(request: FixtureRequest, tmp_path: Path) -> Path:
    path = Path(request.path.parent)
    if path.name != "tests":
        while path.name != "tests":
            path = path.parent
    path /= "data"
    copy_tree(str(path), str(tmp_path))
    return tmp_path


@pytest.fixture()
def test_case_dir(request: FixtureRequest, tmp_path: Path) -> Path:
    path = Path(request.path.parent) / request.path.stem
    copy_tree(str(path), str(tmp_path))
    return tmp_path


@pytest.fixture()
def test_method_dir(request: FixtureRequest, tmp_path: Path) -> Path:
    path = Path(request.path.parent) / request.path.stem / request.node.name
    copy_tree(str(path), str(tmp_path))
    return tmp_path
{% endif %}