# Source: http://blog.recursiveprocess.com/2013/03/14/calculate-pi-with-python/
from timeit import timeit
from decimal import getcontext, Decimal, localcontext
from math import factorial

# Sets decimal to 25 digits of precision
precision = 1000
getcontext().prec = precision + 1

# http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
def plouffBig(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1) / (16 ** k)) * (
            (Decimal(4) / (8 * k + 1))
            - (Decimal(2) / (8 * k + 4))
            - (Decimal(1) / (8 * k + 5))
            - (Decimal(1) / (8 * k + 6))
        )
        k += 1
    return pi

# http://en.wikipedia.org/wiki/Bellard%27s_formula
def bellardBig(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1) ** k / (1024 ** k)) * (
            Decimal(256) / (10 * k + 1)
            + Decimal(1) / (10 * k + 9)
            - Decimal(64) / (10 * k + 3)
            - Decimal(32) / (4 * k + 1)
            - Decimal(4) / (10 * k + 5)
            - Decimal(4) / (10 * k + 7)
            - Decimal(1) / (4 * k + 3)
        )
        k += 1
    pi = pi * 1 / (2 ** 6)
    return pi

# http://en.wikipedia.org/wiki/Chudnovsky_algorithm
def chudnovskyBig(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1) ** k) * (
            Decimal(factorial(6 * k))
            / ((factorial(k) ** 3) * (factorial(3 * k)))
            * (13591409 + 545140134 * k)
            / (640320 ** (3 * k))
        )
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)
    return pi


def test_perf():
    for i in [precision]:  # range(precision, precision + 5):
        print("Iteration number ", i)
        for f in [plouffBig, bellardBig, chudnovskyBig]:
            print(timeit("pi = f(i)", globals=dict(f=plouffBig, i=i), number=10))

        with localcontext() as ctx:
            ctx.prec = 1001
            ans = plouffBig(i)
            print(f"{ans:3g}")
