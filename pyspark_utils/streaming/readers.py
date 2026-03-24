from pyspark.sql import SparkSession, DataFrame

def read_kafka(
    spark: SparkSession,
    servers: str,
    topic: str,
    starting_offsets="latest"
) -> DataFrame:
    return (
        spark.readStream
            .format("kafka")
            .option("kafka.bootstrap.servers", servers)
            .option("subscribe", topic)
            .option("startingOffsets", starting_offsets)
            .load()
    )


def read_autoloader(
    spark: SparkSession,
    path: str,
    schema_location: str
) -> DataFrame:
    return (
        spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "json")
            .option("cloudFiles.schemaLocation", schema_location)
            .load(path)
    )


def read_delta(spark: SparkSession, path: str) -> DataFrame:
    return spark.readStream.format("delta").load(path)
