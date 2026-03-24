from pyspark.sql import DataFrame
import re

def standardize_column_names(df: DataFrame, case: str = "snake") -> DataFrame:
    """
    Standardizes column names to snake_case or lowerCamelCase.
    """
    def to_snake(name):
        name = re.sub(r'[^0-9a-zA-Z]+', '_', name)
        return name.lower()

    def to_camel(name):
        parts = re.sub(r'[^0-9a-zA-Z]+', '_', name).split('_')
        return parts[0].lower() + ''.join(p.capitalize() for p in parts[1:])

    converter = to_snake if case == "snake" else to_camel
    new_cols = [converter(c) for c in df.columns]

    return df.toDF(*new_cols)


def rename_columns(df: DataFrame, mapping: dict) -> DataFrame:
    """
    Renames columns based on a provided mapping.
    """
    for old, new in mapping.items():
        df = df.withColumnRenamed(old, new)
    return df


def trim_column_names(df: DataFrame) -> DataFrame:
    """
    Removes leading/trailing whitespace from column names.
    """
    new_cols = [c.strip() for c in df.columns]
    return df.toDF(*new_cols)
