n = int(input())
res = {}

for _ in range(n):
    key, val = input().split()
    res[key] = f"{key}:{val}"

print(res)