a = set(input().split())
b = set(input().split())

result = sorted(a - b)
print(*result)
