from pyspark.sql import DataFrame

def write_parquet(df: DataFrame, path: str, mode="overwrite", partition_by=None):
    writer = df.write.mode(mode)
    if partition_by:
        writer = writer.partitionBy(partition_by)
    writer.parquet(path)


def write_delta(df: DataFrame, path: str, mode="overwrite", partition_by=None):
    writer = df.write.format("delta").mode(mode)
    if partition_by:
        writer = writer.partitionBy(partition_by)
    writer.save(path)


def safe_overwrite(df: DataFrame, path: str):
    """
    Deletes the target path before writing.
    Useful for idempotent pipelines.
    """
    import shutil
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass

    df.write.mode("overwrite").parquet(path)
