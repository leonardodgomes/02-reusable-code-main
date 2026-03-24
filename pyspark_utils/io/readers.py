from pyspark.sql import DataFrame, SparkSession

def read_csv(spark: SparkSession, path: str, header=True, infer_schema=True, sep=",") -> DataFrame:
    return (
        spark.read
            .option("header", header)
            .option("inferSchema", infer_schema)
            .option("sep", sep)
            .csv(path)
    )


def read_json(spark: SparkSession, path: str, multiline=False) -> DataFrame:
    return spark.read.option("multiline", multiline).json(path)


def read_parquet(spark: SparkSession, path: str) -> DataFrame:
    return spark.read.parquet(path)


def read_delta(spark: SparkSession, path: str, version=None) -> DataFrame:
    if version:
        return spark.read.format("delta").option("versionAsOf", version).load(path)
    return spark.read.format("delta").load(path)


def read_jdbc(spark: SparkSession, url: str, table: str, properties: dict) -> DataFrame:
    return spark.read.jdbc(url=url, table=table, properties=properties)
