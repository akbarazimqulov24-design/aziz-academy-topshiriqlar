nums = [int(x) for x in input().split()]
kvadratlar = sorted({x**2 for x in nums})
print(*kvadratlar)
