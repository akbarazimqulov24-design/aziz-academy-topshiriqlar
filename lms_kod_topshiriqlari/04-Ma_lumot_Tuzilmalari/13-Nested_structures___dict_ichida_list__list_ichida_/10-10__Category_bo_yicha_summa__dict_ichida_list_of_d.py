n = int(input().strip())
res = {}

for _ in range(n):
    cat, name, price, qty = input().split()
    res[cat] = res.get(cat, 0) + int(price) * int(qty)
    
for cat in sorted(res):
    print(cat, res[cat])
    


