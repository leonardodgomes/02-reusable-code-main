from pyspark.sql import DataFrame

def count_rows(df: DataFrame) -> int:
    return df.count()


def print_schema(df: DataFrame):
    df.printSchema()


def show_sample(df: DataFrame, n=5):
    df.show(n, truncate=False)
