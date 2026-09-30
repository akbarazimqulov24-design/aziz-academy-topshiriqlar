n = int(input())
data = [input().split() for _ in range(n)]
result = {k: int(v) * 2 for k, v in data}
print(result)
