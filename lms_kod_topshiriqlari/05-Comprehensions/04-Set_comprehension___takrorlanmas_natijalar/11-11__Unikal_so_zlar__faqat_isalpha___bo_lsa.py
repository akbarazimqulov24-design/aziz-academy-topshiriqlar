words = input().split()
res = sorted({w.lower() for w in words if w.isalpha()})

if res:
    print(*res)
else:
    print("BO'SH")