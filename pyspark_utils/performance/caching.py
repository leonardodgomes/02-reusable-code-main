from pyspark.sql import DataFrame

def cache_if_small(df: DataFrame, threshold_mb: int = 500) -> DataFrame:
    """
    Caches the DataFrame only if it's below a size threshold.
    """
    size_in_bytes = df.storageLevel.useMemory
    if size_in_bytes and size_in_bytes < threshold_mb * 1024 * 1024:
        df.cache()
    return df


def uncache(df: DataFrame):
    """
    Safely uncache a DataFrame.
    """
    try:
        df.unpersist()
    except Exception:
        pass
