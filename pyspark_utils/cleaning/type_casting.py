from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def cast_columns(df: DataFrame, schema_dict: dict) -> DataFrame:
    """
    Casts columns to specified types: {"col": "integer"}.
    """
    for c, t in schema_dict.items():
        df = df.withColumn(c, col(c).cast(t))
    return df


def safe_cast(df: DataFrame, column: str, dtype: str) -> DataFrame:
    """
    Casts a column safely, replacing invalid values with null.
    """
    return df.withColumn(column, col(column).cast(dtype))
