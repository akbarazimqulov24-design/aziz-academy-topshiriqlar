a, b = input().strip(), input().strip()
res = sorted(set(a) & set(b))

print("".join(res) if res else "BO'SH")