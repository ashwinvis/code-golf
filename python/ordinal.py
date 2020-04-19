import sys


suffix = {1: "st", 2: "nd", 3: "rd", 11: "th", 12: "th", 13: "th"}

for n in sys.argv[1:]:
    get_suffix = lambda base, default: suffix[rem] if (rem := int(n) % base) in suffix else default
    print(f"{n}{get_suffix(100, '') or get_suffix(10, 'th')}")
