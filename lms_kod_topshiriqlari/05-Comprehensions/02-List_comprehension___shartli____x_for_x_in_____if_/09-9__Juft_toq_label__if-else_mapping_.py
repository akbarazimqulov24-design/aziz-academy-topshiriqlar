nums = map(int, input().split())
tabels = ['even' if x % 2 == 0 else 'odd' for x in nums]
print(*tabels)
