for i in range(1,101):
    if (i % sum(map(int, str(i)))) == 0:
        print(i)
