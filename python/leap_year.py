for n in range(1800, 2401):
    divisible = lambda x, y: x % y == 0
    # XOR logic: Leap year = D4 - (D100 + D400)
    if divisible(n, 4) ^ divisible(n, 100) ^ divisible(n, 400):
        print(n)
