n = int(input())
d = {}

for _ in range(n):
    item, price = input().split()
    d[item] = int(price)
    
print(sum(d.values()))    