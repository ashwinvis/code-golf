# https://stackoverflow.com/questions/4484489/using-basic-arithmetics-for-calculating-pi-with-arbitary-precision
from decimal import *


getcontext().prec = 1001
pi = 0
D = Decimal
for k in range(1001):
    pi += (D(1) / (16 ** k)) * (
        (D(4) / (8 * k + 1))
        - (D(2) / (8 * k + 4))
        - (D(1) / (8 * k + 5))
        - (D(1) / (8 * k + 6))
    )
print(pi)
