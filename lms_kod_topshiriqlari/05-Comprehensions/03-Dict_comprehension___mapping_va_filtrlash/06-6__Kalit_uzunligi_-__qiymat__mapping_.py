n = int(input())
data = [input().split() for _ in range(n)]
result = {len(k): int(v) for k, v in data}
print(result)
