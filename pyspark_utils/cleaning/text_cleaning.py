from pyspark.sql import DataFrame
from pyspark.sql.functions import trim, regexp_replace, col

def trim_strings(df: DataFrame) -> DataFrame:
    """
    Trims whitespace from all string columns.
    """
    for c, t in df.dtypes:
        if t == "string":
            df = df.withColumn(c, trim(col(c)))
    return df


def remove_special_characters(df: DataFrame, columns: list) -> DataFrame:
    """
    Removes non-alphanumeric characters from selected columns.
    """
    for c in columns:
        df = df.withColumn(c, regexp_replace(col(c), r"[^a-zA-Z0-9 ]", ""))
    return df


def normalize_whitespace(df: DataFrame, columns: list) -> DataFrame:
    """
    Replaces multiple spaces with a single space.
    """
    for c in columns:
        df = df.withColumn(c, regexp_replace(col(c), r"\s+", " "))
    return df
