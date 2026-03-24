from delta.tables import DeltaTable
from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp, lit

def merge_upsert(spark, df: DataFrame, target_path: str, keys: list):
    """
    Realiza um MERGE (upsert) simples.
    """
    delta_table = DeltaTable.forPath(spark, target_path)

    (
        delta_table.alias("t")
        .merge(
            df.alias("s"),
            " AND ".join([f"t.{k} = s.{k}" for k in keys])
        )
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )


def merge_scd2(spark, df: DataFrame, target_path: str, keys: list, start_col="start_date", end_col="end_date"):
    """
    Implementa SCD2 (Slowly Changing Dimension Type 2).
    """
    delta_table = DeltaTable.forPath(spark, target_path)

    (
        delta_table.alias("t")
        .merge(
            df.alias("s"),
            " AND ".join([f"t.{k} = s.{k}" for k in keys])
        )
        .whenMatchedUpdate(set={
            end_col: current_timestamp()
        })
        .whenNotMatchedInsertAll()
        .execute()
    )
