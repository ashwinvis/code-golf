import sys


suffix = {1: "st", 2: "nd", 3: "rd"}
suffix2 = {11: "th", 12: "th", 13: "th"}

for n in sys.argv[1:]:
    th = suffix[rem] if (rem := (m:=int(n)) % 10) in suffix else "th"
    th2 = suffix2[rem] if (rem := m % 100) in suffix2 else ""
    print(f"{n}{th2 or th}")
