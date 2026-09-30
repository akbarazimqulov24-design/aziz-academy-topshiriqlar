n = int(input())
data = [input().split() for _ in range(n)]
result = {k: int(v) for k, v in data if int(v) > 10}
print(result)