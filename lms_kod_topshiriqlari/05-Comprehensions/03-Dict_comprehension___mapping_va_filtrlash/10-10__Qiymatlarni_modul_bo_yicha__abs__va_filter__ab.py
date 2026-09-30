n = int(input())
data = [input().split() for _ in range(n)]
result = {k: abs(int(v)) for k, v in data if abs(int(v)) >= 5}
print(result)