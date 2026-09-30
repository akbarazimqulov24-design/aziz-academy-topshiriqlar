n = int(input())
data = [input().split() for _ in range(n)]
result = {k: str(v) for k, v in data}
print(result)
