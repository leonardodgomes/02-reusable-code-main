from pyspark.sql import DataFrame

def explain_performance(df: DataFrame):
    """
    Prints a formatted explain plan.
    """
    print("\n=== EXECUTION PLAN ===")
    df.explain(True)
