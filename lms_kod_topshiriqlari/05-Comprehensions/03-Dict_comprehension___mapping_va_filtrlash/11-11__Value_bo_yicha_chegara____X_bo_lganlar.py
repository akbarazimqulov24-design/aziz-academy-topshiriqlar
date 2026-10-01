n = int(input())
data = {}

for _ in range(n):
    key, val = input().split()
    data[key] = int(val)
    
X = int(input())

res = {k: v for k, v in data.items() if v >= X}
print(res)
