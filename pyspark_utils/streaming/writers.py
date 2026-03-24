from pyspark.sql import DataFrame

def write_delta(
    df: DataFrame,
    path: str,
    checkpoint: str,
    mode="append"
):
    return (
        df.writeStream
            .format("delta")
            .option("checkpointLocation", checkpoint)
            .outputMode(mode)
            .start(path)
    )


def write_console(df: DataFrame):
    return (
        df.writeStream
            .format("console")
            .option("truncate", False)
            .start()
    )


def write_memory(df: DataFrame, table_name: str):
    return (
        df.writeStream
            .format("memory")
            .queryName(table_name)
            .outputMode("append")
            .start()
    )
