"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    result_cache = dict()

    def cached_func(*args) -> Callable:
        if args in result_cache:
            return result_cache[args]
        result = func(*args)
        result_cache[args] = result
        return result

    return cached_func
