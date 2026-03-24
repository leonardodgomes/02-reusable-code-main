def optimize_table(spark, path: str):
    spark.sql(f"OPTIMIZE delta.`{path}`")


def optimize_zorder(spark, path: str, columns: list):
    cols = ", ".join(columns)
    spark.sql(f"OPTIMIZE delta.`{path}` ZORDER BY ({cols})")
