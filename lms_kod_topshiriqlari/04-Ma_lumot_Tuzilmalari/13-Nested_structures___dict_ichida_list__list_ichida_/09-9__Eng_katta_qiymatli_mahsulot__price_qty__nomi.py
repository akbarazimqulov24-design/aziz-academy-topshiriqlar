n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

best = max(items, key=lambda x: x['price'] * x['qty'])
print(best['name'])
