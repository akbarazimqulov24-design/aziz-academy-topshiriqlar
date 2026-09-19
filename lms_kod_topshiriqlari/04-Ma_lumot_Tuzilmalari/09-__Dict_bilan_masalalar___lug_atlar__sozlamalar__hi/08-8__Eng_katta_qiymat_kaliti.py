n = int(input())
items = [input().split() for _ in range(n)]
print(max(items, key=lambda x: int(x[1]))[0])