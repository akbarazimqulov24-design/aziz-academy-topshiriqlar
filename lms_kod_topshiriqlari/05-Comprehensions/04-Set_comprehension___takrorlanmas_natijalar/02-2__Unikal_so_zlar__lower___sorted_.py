words = input().split()
unikal = sorted({w.lower() for w in words})
print(*unikal)