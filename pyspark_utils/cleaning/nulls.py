from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

def fill_nulls(df: DataFrame, rules: dict) -> DataFrame:
    """
    Fills null values based on a mapping: {column: value}.
    """
    return df.fillna(rules)


def drop_nulls(df: DataFrame, subset: list = None) -> DataFrame:
    """
    Drops rows with nulls in specific columns.
    """
    return df.dropna(subset=subset)


def replace_nulls_with_default(df: DataFrame, default_map: dict) -> DataFrame:
    """
    Replaces nulls with default values using when/otherwise.
    """
    for col_name, default_value in default_map.items():
        df = df.withColumn(
            col_name,
            col(col_name).otherwise(lit(default_value))
        )
    return df
