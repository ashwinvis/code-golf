for i in range(1,101):
    s = 0
    j = i
    while j:
        s += j % 10
        j //= 10
    if (i % s) == 0:
        print(i)
