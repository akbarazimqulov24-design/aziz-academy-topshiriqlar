n = int(input())

d = {}
for _ in range(n):
    key, val = input().split()
    d[key] = val

target_key = input()
print(d[target_key])