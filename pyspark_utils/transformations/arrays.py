from pyspark.sql import DataFrame
from pyspark.sql.functions import array_distinct, size, col

def array_size(df: DataFrame, column: str) -> DataFrame:
    return df.withColumn(f"{column}_size", size(col(column)))


def array_unique(df: DataFrame, column: str) -> DataFrame:
    return df.withColumn(column, array_distinct(col(column)))
