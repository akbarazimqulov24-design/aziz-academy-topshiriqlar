n = int(input())

d = {}
for _ in range(n):
    key, val = input().split()
    d[key] = val
    
for key in sorted(d):
    print(f"{key}={d[key]}")