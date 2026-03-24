from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def select_before_join(df: DataFrame, columns: list) -> DataFrame:
    """
    Reduz o tamanho do DataFrame antes de um join,
    selecionando apenas as colunas necessárias.
    """
    return df.select([col(c) for c in columns])


def drop_before_join(df: DataFrame, columns: list) -> DataFrame:
    """
    Remove colunas pesadas antes de um join para evitar shuffles grandes.
    """
    return df.drop(*columns)


def repartition_on_key(df: DataFrame, key: str) -> DataFrame:
    """
    Reparticiona o DataFrame pelo join key para evitar shuffles desnecessários.
    """
    return df.repartition(key)


def coalesce_after_filter(df: DataFrame, num_partitions: int = 1) -> DataFrame:
    """
    Após filtros que reduzem muito o dataset, reduz o número de partições.
    """
    return df.coalesce(num_partitions)


def avoid_wide_transformations(df: DataFrame) -> DataFrame:
    """
    Exemplo de função que alerta sobre operações que causam wide shuffles.
    (Não altera o DF, apenas serve como documentação/boas práticas.)
    """
    print("""
    ⚠️ Evite estas operações sem necessidade:
    - groupBy sem partitioning adequado
    - distinct em datasets grandes
    - joins sem repartition
    - orderBy global
    - explode em arrays muito grandes
    """)
    return df


def pre_filter_before_join(df: DataFrame, condition: str) -> DataFrame:
    """
    Filtra o DataFrame antes de um join para reduzir o volume de dados.
    """
    return df.filter(condition)
