import time
from functools import wraps

def timeit(func):
    """
    Mede o tempo de execução de uma função.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMEIT] {func.__name__} executou em {end - start:.2f}s")
        return result
    return wrapper


def retry(times=3, delay=1):
    """
    Tenta executar a função várias vezes em caso de erro.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[RETRY] Tentativa {attempt+1}/{times} falhou: {e}")
                    time.sleep(delay)
            raise Exception(f"Função falhou após {times} tentativas")
        return wrapper
    return decorator
