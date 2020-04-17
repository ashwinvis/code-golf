def fib(n):
    return int(bool(n)) if n < 3 else fib(n-1) + fib(n-2)

for i in range(31):
    print(fib(i))
