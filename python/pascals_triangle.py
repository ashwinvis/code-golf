from math import *

for order in range(20):
    for degree in range(order + 1):
        print(comb(order, degree), end=" ")
    print()
