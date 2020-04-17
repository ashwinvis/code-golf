from functools import lru_cache

@lru_cache
def fib(n):
    return int(bool(n)) if n in (0, 1, 2) else fib(n-1) + fib(n-2)

for i in range(31):
    print(fib(i))
