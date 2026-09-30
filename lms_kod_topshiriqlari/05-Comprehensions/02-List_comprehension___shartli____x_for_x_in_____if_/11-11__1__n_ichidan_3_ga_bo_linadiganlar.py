n = int(input())
res = [i for i in range(1, n + 1) if i % 3 == 0]
print(*res if res else ["BO'SH"])