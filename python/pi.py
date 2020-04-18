# https://stackoverflow.com/questions/4484489/using-basic-arithmetics-for-calculating-pi-with-arbitary-precision
from decimal import getcontext, Decimal


getcontext().prec = 1001
pi = 0
for k in range(1001):
    pi += (Decimal(1) / (16 ** k)) * (
        (Decimal(4) / (8 * k + 1))
        - (Decimal(2) / (8 * k + 4))
        - (Decimal(1) / (8 * k + 5))
        - (Decimal(1) / (8 * k + 6))
    )
print(pi)
