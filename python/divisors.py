for xs in range(1, 101):
    print(" ".join(d for d in range(1, xs+1) if xs % d < 1))
    #  for divs in range(1, xs+1):
    #      if xs % divs < 1:
    #          print(divs, end=" ")
    #  print()

#  sprint = lambda xs : print(" ".join(str(x) for x in xs))
#  list(map(lambda xs: sprint(filter(lambda div: xs % div < 1, range(1, xs+1))), range(1, 101)))
