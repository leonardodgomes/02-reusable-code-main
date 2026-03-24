from pyspark.sql import DataFrame, Window
from pyspark.sql.functions import row_number, rank, dense_rank, col, sum, first, last, lag, lead



def row_number_by(df: DataFrame, partition_cols: list, order_col: str, ascending=False):
    """
    Adds a row_number column based on partition and order.
    """
    order = col(order_col).asc() if ascending else col(order_col).desc()
    w = Window.partitionBy(*partition_cols).orderBy(order)
    return df.withColumn("row_number", row_number().over(w))



def latest_record(df: DataFrame, keys: list, order_by: str):
    """
    Returns only the latest record per key.
    """
    w = Window.partitionBy(*keys).orderBy(col(order_by).desc())
    return (
        df.withColumn("_rn", row_number().over(w))
          .filter("_rn = 1")
          .drop("_rn")
    )



def rolling_sum(df: DataFrame, partition_cols: list, order_col: str, target_col: str):
    """
    Computes a cumulative sum over a window.
    """
    w = (
        Window.partitionBy(*partition_cols)
              .orderBy(order_col)
              .rowsBetween(Window.unboundedPreceding, Window.currentRow)
    )
    return df.withColumn(f"{target_col}_rolling_sum", sum(target_col).over(w))




def first_last(df: DataFrame, partition_cols: list, order_col: str, target_col: str):
    """
    Adds first and last values of a column within a partition.
    """
    w = Window.partitionBy(*partition_cols).orderBy(order_col)

    return (
        df.withColumn(f"{target_col}_first", first(target_col).over(w))
          .withColumn(f"{target_col}_last", last(target_col).over(w))
    )



def add_lag(df: DataFrame, column: str, offset: int, partition_cols: list, order_col: str):
    w = Window.partitionBy(*partition_cols).orderBy(order_col)
    return df.withColumn(f"{column}_lag_{offset}", lag(column, offset).over(w))


def add_lead(df: DataFrame, column: str, offset: int, partition_cols: list, order_col: str):
    w = Window.partitionBy(*partition_cols).orderBy(order_col)
    return df.withColumn(f"{column}_lead_{offset}", lead(column, offset).over(w))
