from pyspark.sql import DataFrame

def with_watermark(df: DataFrame, column: str, delay: str):
    return df.withWatermark(column, delay)
