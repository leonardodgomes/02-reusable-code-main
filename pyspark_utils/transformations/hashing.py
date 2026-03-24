from pyspark.sql import DataFrame
from pyspark.sql.functions import sha2, concat_ws, col

def hash_columns(df: DataFrame, columns: list, bits: int = 256) -> DataFrame:
    """
    Hashes multiple columns into a single fingerprint.
    """
    return df.withColumn(
        "hash_value",
        sha2(concat_ws("||", *[col(c) for c in columns]), bits)
    )
