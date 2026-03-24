import json
from pyspark.sql.types import StructType

def load_schema_from_json(path: str) -> StructType:
    """
    Loads a Spark schema from a JSON file.
    """
    with open(path, "r") as f:
        schema_json = json.load(f)
    return StructType.fromJson(schema_json)


def enforce_schema(df, schema: StructType):
    """
    Applies a schema to a DataFrame using selectExpr.
    """
    return df.select([c.name for c in schema])
