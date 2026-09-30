nums = map(int, input().split())
tabels = ['pos' if x > 0 else 'neg' if x < 0 else 'zero' for x in nums]
print(*tabels)
