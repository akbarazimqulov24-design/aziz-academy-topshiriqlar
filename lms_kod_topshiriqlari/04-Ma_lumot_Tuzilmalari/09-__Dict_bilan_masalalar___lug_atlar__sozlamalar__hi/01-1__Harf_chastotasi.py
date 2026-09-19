s = input().strip()
print(*(f"{c}:{s.count(c)}" for c in dict.fromkeys(s)))
