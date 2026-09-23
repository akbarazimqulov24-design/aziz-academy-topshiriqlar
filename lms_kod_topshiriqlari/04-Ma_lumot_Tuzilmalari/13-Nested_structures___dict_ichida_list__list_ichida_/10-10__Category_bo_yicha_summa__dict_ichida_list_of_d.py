n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})

totals = {}
for x in items:
    totals[x['cat']] = totals.get(x['cat'], 0) + x['price'] * x['qty']
    
for cat in sorted(totals):
    print(cat, totals[cat])