n = int(input())
data = [input().split() for _ in range(n)]
result = {k.upper(): int(v) for k, v in data}
print(result)
