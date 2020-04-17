from sys import argv
suffix = {"1": "st", "2": "nd", "3": "rd"}
for n in argv:
    th = suffix[n] if str(n)[-1] in suffix else "th"
    print(f"{n}{th}")
