msg = {3: "Fizz", 5: "Buzz"}

for i in range(1,101):
    activated = False
    for j in m:
        if not i % j:
            activated = True
            print(msg[j], end="")

    end = "" if activated else i
    print(end)
