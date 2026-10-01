nums = [int(x) for x in input().split()]
juft = sorted({x for x in nums if x % 2 == 0})

if juft:
    print(*juft)
else:
    print("BO'SH")
