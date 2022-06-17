{% if cookiecutter.pyspark_version -%}
from distutils.dir_util import copy_tree
from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark(request: FixtureRequest) -> SparkSession:
    # https://github.com/malexer/pytest-spark/issues/9#issue-434176947

    spark_ = (
        SparkSession.builder.master("local[*]")
        .config("spark.sql.shuffle.partitions", 1)
        .config("spark.default.parallelism", 1)
        .config("spark.rdd.compress", False)
        .config("spark.shuffle.compress", False)
        .config("spark.ui.showConsoleProgress", False)
        .getOrCreate()
    )
    # https://stackoverflow.com/questions/40608412/how-can-set-the-default-spark-logging-level
    # spark_.sparkContext.setLogLevel("info")

    request.addfinalizer(lambda: spark_.sparkContext.stop())
    return spark_


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
