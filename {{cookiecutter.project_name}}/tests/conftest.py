{% if cookiecutter.pyspark_version -%}
import os

import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master(os.environ["SPARK_MASTER"]).appName("{{cookiecutter.project_name}}").getOrCreate()
{% endif %}