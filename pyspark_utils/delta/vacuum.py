def vacuum_table(spark, path: str, retention_hours=168):
    spark.sql(f"VACUUM delta.`{path}` RETAIN {retention_hours} HOURS")
