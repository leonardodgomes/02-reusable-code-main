from pyspark.sql import DataFrame

def pivot_table(df: DataFrame, index: list, column: str, value: str):
    """
    Creates a pivot table.
    """
    return df.groupBy(index).pivot(column).sum(value)
