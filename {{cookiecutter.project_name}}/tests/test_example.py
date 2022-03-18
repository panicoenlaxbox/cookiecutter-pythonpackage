{% if cookiecutter.pyspark_version -%}
import pytest
from assertpy import assert_that
from chispa import assert_df_equality
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType


@pytest.mark.spark()
def test_spark_installation(spark: SparkSession):
    assert_that(spark.conf.get("spark.master")).is_equal_to("local")


@pytest.mark.spark()
def test_spark(spark: SparkSession):
    data = [("Sergio", 45), ("Carmen", 44)]
    schema = StructType(
        [StructField("name", StringType(), nullable=False), StructField("age", IntegerType(), nullable=False)]
    )

    actual = spark.createDataFrame(data, schema)

    expected = spark.createDataFrame(data, schema)
    assert_df_equality(actual, expected)
{% else -%}
from assertpy import assert_that


def test_example():
    assert_that(True).is_true()
{% endif %}