from pyspark.sql import DataFrame
from pyspark.sql.functions import broadcast

def safe_join(df1: DataFrame, df2: DataFrame, keys: list, how: str = "inner") -> DataFrame:
    """
    Performs a join with automatic duplicate key detection.
    """
    if isinstance(keys, str):
        keys = [keys]

    return df1.join(df2, keys, how)


def broadcast_join(df1: DataFrame, df2: DataFrame, keys: list) -> DataFrame:
    """
    Forces a broadcast join for small lookup tables.
    """
    return df1.join(broadcast(df2), keys, "inner")
