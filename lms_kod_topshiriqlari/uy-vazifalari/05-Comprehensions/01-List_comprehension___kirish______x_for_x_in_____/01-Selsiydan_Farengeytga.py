nums = list(map(int, input().split()))

res = [c * 9 // 5 + 32 for c in nums]

print(res)