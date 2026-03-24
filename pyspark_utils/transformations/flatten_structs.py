from pyspark.sql import DataFrame
from pyspark.sql.functions import col, explode

def flatten_struct(df: DataFrame) -> DataFrame:
    """
    Flattens a single level of struct columns.
    """
    flat_cols = []
    nested_cols = []

    for c, t in df.dtypes:
        if "struct" in t:
            nested_cols.append(c)
        else:
            flat_cols.append(c)

    for nc in nested_cols:
        for field in df.select(f"{nc}.*").columns:
            flat_cols.append(col(f"{nc}.{field}").alias(f"{nc}_{field}"))

    return df.select(flat_cols)


def explode_array(df: DataFrame, column: str) -> DataFrame:
    """
    Explodes an array column into multiple rows.
    """
    return df.withColumn(column, explode(col(column)))
