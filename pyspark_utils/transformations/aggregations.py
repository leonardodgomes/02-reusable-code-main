from pyspark.sql import DataFrame
from pyspark.sql.functions import sum, count, avg

def aggregate_by(df: DataFrame, group_cols: list, agg_map: dict) -> DataFrame:
    """
    Generic aggregation function.
    agg_map example: {"premium": "sum", "claim_amount": "avg"}
    """
    agg_exprs = []

    for col_name, func in agg_map.items():
        if func == "sum":
            agg_exprs.append(sum(col_name).alias(f"{col_name}_sum"))
        elif func == "avg":
            agg_exprs.append(avg(col_name).alias(f"{col_name}_avg"))
        elif func == "count":
            agg_exprs.append(count(col_name).alias(f"{col_name}_count"))

    return df.groupBy(group_cols).agg(*agg_exprs)
