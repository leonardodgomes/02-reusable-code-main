from pyspark.sql import DataFrame

def create_or_replace_table(df: DataFrame, path: str, partition_by=None):
    writer = df.write.format("delta").mode("overwrite")
    if partition_by:
        writer = writer.partitionBy(partition_by)
    writer.save(path)


def read_table(spark, path: str):
    return spark.read.format("delta").load(path)
