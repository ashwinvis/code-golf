for n in range(1800, 2401):
    divisible = lambda y: n % y == 0
    # XOR logic: Leap year = D4 - (D100 + D400)
    if divisible(4) ^ divisible(100) ^ divisible(400):
        print(n)
