n = int(input())
res = {}

for _ in range(n):
    key, val = input().split()
    res[key[::-1]] = int(val)
    
print(res)
