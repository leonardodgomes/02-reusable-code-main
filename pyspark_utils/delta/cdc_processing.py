from delta.tables import DeltaTable
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, current_timestamp, lit


def apply_cdc(
    spark,
    df_cdc: DataFrame,
    target_path: str,
    key: str,
    operation_col: str = "op"
):
    """
    Aplica CDC (Change Data Capture) em uma tabela Delta.
    O DataFrame df_cdc deve conter uma coluna de operação:
        - 'I' = Insert
        - 'U' = Update
        - 'D' = Delete
    """
    delta_table = DeltaTable.forPath(spark, target_path)

    (
        delta_table.alias("t")
        .merge(
            df_cdc.alias("s"),
            f"t.{key} = s.{key}"
        )
        .whenMatchedUpdate(
            condition=f"s.{operation_col} = 'U'",
            set={c: f"s.{c}" for c in df_cdc.columns if c != operation_col}
        )
        .whenMatchedDelete(
            condition=f"s.{operation_col} = 'D'"
        )
        .whenNotMatchedInsert(
            condition=f"s.{operation_col} = 'I'",
            values={c: f"s.{c}" for c in df_cdc.columns if c != operation_col}
        )
        .execute()
    )


def apply_soft_delete(
    spark,
    df_cdc: DataFrame,
    target_path: str,
    key: str,
    deleted_flag_col: str = "is_deleted",
    operation_col: str = "op"
):
    """
    Aplica soft delete usando uma coluna booleana.
    """
    delta_table = DeltaTable.forPath(spark, target_path)

    (
        delta_table.alias("t")
        .merge(
            df_cdc.alias("s"),
            f"t.{key} = s.{key}"
        )
        .whenMatchedUpdate(
            condition=f"s.{operation_col} = 'D'",
            set={deleted_flag_col: lit(True)}
        )
        .whenMatchedUpdate(
            condition=f"s.{operation_col} = 'U'",
            set={c: f"s.{c}" for c in df_cdc.columns if c != operation_col}
        )
        .whenNotMatchedInsert(
            condition=f"s.{operation_col} = 'I'",
            values={c: f"s.{c}" for c in df_cdc.columns if c != operation_col}
        )
        .execute()
    )


def apply_cdc_scd2(
    spark,
    df_cdc: DataFrame,
    target_path: str,
    key: str,
    start_col="start_date",
    end_col="end_date",
    operation_col="op"
):
    """
    Aplica CDC com SCD2.
    """
    delta_table = DeltaTable.forPath(spark, target_path)

    (
        delta_table.alias("t")
        .merge(
            df_cdc.alias("s"),
            f"t.{key} = s.{key}"
        )
        .whenMatchedUpdate(
            condition=f"s.{operation_col} = 'U'",
            set={end_col: current_timestamp()}
        )
        .whenNotMatchedInsert(
            condition=f"s.{operation_col} IN ('I', 'U')",
            values={
                **{c: f"s.{c}" for c in df_cdc.columns if c != operation_col},
                start_col: current_timestamp(),
                end_col: lit(None)
            }
        )
        .execute()
    )
