for i in range(1,101):
    s = sum(int(digit) for digit in str(i))
    if (i % s) == 0:
        print(i)
