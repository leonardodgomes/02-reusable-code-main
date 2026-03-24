class PipelineError(Exception):
    """Erro genérico de pipeline."""
    pass


class SchemaMismatchError(Exception):
    """Erro quando o schema não corresponde ao esperado."""
    pass
