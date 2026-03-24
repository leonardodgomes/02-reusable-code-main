from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, when

def check_nulls(df: DataFrame, columns: list) -> DataFrame:
    """
    Returns a DataFrame with null counts for each column.
    """
    exprs = [count(when(col(c).isNull(), c)).alias(c) for c in columns]
    return df.agg(*exprs)


def check_unique(df: DataFrame, columns: list) -> bool:
    """
    Returns True if the combination of columns is unique.
    """
    total = df.count()
    distinct = df.select(columns).distinct().count()
    return total == distinct


def check_value_ranges(df: DataFrame, column: str, min_val, max_val) -> bool:
    """
    Checks if all values in a column fall within a range.
    """
    invalid = df.filter((col(column) < min_val) | (col(column) > max_val)).count()
    return invalid == 0
