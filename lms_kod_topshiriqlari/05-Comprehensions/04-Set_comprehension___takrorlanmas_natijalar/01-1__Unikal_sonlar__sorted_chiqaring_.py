nums = [int(x) for x in input().split()]
unikal = sorted({x for x in nums})
print(*unikal)