# cast-service/app/api/util.py

import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: Calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_func = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')
        return original_func
    return wrapper
