nums = [int(x) for x in input().split()]
res = sorted({abs(x) for x in nums})
print(*res)