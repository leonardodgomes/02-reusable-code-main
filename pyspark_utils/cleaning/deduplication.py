from pyspark.sql import DataFrame, Window
from pyspark.sql.functions import row_number, col

def dedupe(df: DataFrame, keys: list, order_by: str) -> DataFrame:
    """
    Deduplicates rows using keys and keeps the latest based on order_by.
    """
    w = Window.partitionBy(*keys).orderBy(col(order_by).desc())
    return df.withColumn("_rn", row_number().over(w)).filter("_rn = 1").drop("_rn")


def drop_exact_duplicates(df: DataFrame) -> DataFrame:
    """
    Drops exact duplicate rows.
    """
    return df.dropDuplicates()
