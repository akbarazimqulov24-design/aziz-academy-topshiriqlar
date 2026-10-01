n = int(input())
res = sorted({x for x in range(1, n + 1) if x % 3 == 0})

if res:
    print(*res)
else:
    print("BO'SH")