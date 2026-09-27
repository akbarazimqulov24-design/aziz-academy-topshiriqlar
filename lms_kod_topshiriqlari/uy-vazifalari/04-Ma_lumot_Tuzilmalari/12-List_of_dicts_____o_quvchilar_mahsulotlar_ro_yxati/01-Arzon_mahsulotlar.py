n = int(input())
products = [dict(zip(["name", "price"], input().split())) for _ in range(n)]
limit = int(input())

for p in products:
    if int(p["price"]) < limit:
        print(p["name"])