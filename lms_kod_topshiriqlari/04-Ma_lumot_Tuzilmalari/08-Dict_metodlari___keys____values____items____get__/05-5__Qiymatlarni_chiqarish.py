n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
    
for v in d.values():
    print(v)