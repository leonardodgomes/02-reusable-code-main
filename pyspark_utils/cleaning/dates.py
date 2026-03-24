from pyspark.sql import DataFrame
from pyspark.sql.functions import to_date, col

def standardize_date_formats(df: DataFrame, columns: list, fmt: str = "yyyy-MM-dd") -> DataFrame:
    """
    Converts date columns to a standard format.
    """
    for c in columns:
        df = df.withColumn(c, to_date(col(c), fmt))
    return df


def extract_date_parts(df: DataFrame, column: str) -> DataFrame:
    """
    Adds year, month, day columns from a date column.
    """
    return (
        df.withColumn(f"{column}_year", col(column).year)
          .withColumn(f"{column}_month", col(column).month)
          .withColumn(f"{column}_day", col(column).day)
    )
