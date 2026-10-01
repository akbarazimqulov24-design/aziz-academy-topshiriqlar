n = int(input())
seen = set()
res = {}

for _ in range(n):
    key, val = input().split()
    val = int(val)
    if val not in seen:
        seen.add(val)
        res[key] = val
        
print(res)