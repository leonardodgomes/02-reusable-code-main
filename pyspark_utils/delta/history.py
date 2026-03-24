def show_history(spark, path: str):
    return spark.sql(f"DESCRIBE HISTORY delta.`{path}`")


def read_version(spark, path: str, version: int):
    return spark.read.format("delta").option("versionAsOf", version).load(path)
