from pyspark.sql import DataFrame

def expect_non_null(df: DataFrame, column: str) -> bool:
    return df.filter(f"{column} IS NULL").count() == 0


def expect_positive(df: DataFrame, column: str) -> bool:
    return df.filter(f"{column} <= 0").count() == 0


def expect_valid_status(df: DataFrame, column: str, allowed: list) -> bool:
    return df.filter(~df[column].isin(allowed)).count() == 0
