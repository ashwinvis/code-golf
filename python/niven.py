for i in range(1,101):
    (i % sum(map(int, str(i)))<1) and print(i)
