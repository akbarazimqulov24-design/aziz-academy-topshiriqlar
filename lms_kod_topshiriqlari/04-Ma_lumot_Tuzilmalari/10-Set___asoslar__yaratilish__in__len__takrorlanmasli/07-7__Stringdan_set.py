s = sorted(set(input()))
print("{" + ", ".join(repr(x) for x in s) + "}")
           