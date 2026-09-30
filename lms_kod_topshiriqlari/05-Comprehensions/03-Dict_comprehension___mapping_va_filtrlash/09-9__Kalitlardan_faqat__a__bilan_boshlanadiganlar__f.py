n = int(input())
data = [input().split() for _ in range(n)]
result = {k: int(v) for k, v in data if k.startswith('a')}
print(result)