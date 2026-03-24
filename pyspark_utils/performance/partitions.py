from pyspark.sql import DataFrame

def optimize_shuffle_partitions(spark, df: DataFrame, target_size_mb: int = 128):
    """
    Dynamically adjusts shuffle partitions based on DataFrame size.
    """
    size = df.count()  # simple heuristic
    partitions = max(1, int(size / (target_size_mb * 1000)))
    spark.conf.set("spark.sql.shuffle.partitions", partitions)
    return partitions


def repartition_for_join(df: DataFrame, other_df: DataFrame, key: str) -> DataFrame:
    """
    Repartitions both DataFrames on the join key.
    """
    return df.repartition(key)
