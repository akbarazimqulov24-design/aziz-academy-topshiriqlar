n = int(input())
d = {}

for _ in range(n):
    ism, baho = input().split()
    d[ism] = baho
    
print(*sorted(d.keys()))