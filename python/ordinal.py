import sys


suffix = {1: "st", 2: "nd", 3: "rd"}
suffix2 = {11: "th", 12: "th", 13: "th"}

for n in sys.argv[1:]:
    get_suffix = lambda base, rem2suffix, default: rem2suffix[rem] if (rem := int(n) % base) in rem2suffix else default
    print(f"{n}{get_suffix(100, suffix2, '') or get_suffix(10, suffix, 'th')}")
