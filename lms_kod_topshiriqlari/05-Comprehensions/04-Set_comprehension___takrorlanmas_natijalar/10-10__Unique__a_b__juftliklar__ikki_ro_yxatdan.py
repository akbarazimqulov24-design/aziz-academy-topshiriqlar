A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

juftliklar = sorted({(a, b) for a in A for b in B})

print(len(juftliklar))
for a, b in juftliklar:
    print(f"{a},{b}")