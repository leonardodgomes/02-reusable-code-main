from pyspark.sql import DataFrame
from pyspark.sql.functions import broadcast

def auto_broadcast(df1: DataFrame, df2: DataFrame, keys: list, threshold_mb: int = 100):
    """
    Broadcasts df2 if it's below the threshold.
    """
    size = df2.count()  # simple heuristic
    if size < threshold_mb * 1000:
        return df1.join(broadcast(df2), keys, "inner")
    return df1.join(df2, keys, "inner")
