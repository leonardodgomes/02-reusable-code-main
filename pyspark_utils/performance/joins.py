from pyspark.sql import DataFrame

def sort_merge_join(df1: DataFrame, df2: DataFrame, keys: list, how="inner"):
    """
    Forces a sort-merge join by disabling broadcast.
    """
    df1.sparkSession.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)
    return df1.join(df2, keys, how)
