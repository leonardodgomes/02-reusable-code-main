from pyspark.sql import DataFrame
from pyspark.sql.functions import col, countDistinct, min, max, avg

def profile_dataframe(df: DataFrame) -> dict:
    """
    Returns a dictionary with basic stats for each column.
    """
    profile = {}
    for c, t in df.dtypes:
        stats = df.agg(
            countDistinct(c).alias("distinct"),
            min(c).alias("min"),
            max(c).alias("max")
        ).first()
        profile[c] = {
            "type": t,
            "distinct": stats["distinct"],
            "min": stats["min"],
            "max": stats["max"]
        }
    return profile
