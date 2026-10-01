words = input().split()
harflar = sorted({w[0].lower() for w in words})
print(*harflar)
