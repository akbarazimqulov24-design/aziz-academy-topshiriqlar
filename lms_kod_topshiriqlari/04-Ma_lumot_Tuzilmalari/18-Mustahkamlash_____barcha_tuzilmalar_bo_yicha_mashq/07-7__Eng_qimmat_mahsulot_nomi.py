n = int(input())
products = [{'nom': input(), 'narx': int(input())} for _ in range(n)]

print(max(products, key=lambda d: d['narx'])['nom'])