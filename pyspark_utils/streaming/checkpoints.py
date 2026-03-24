import shutil
import os

def clean_checkpoint(path: str):
    """
    Remove um checkpoint antigo (útil para testes).
    """
    if os.path.exists(path):
        shutil.rmtree(path)
