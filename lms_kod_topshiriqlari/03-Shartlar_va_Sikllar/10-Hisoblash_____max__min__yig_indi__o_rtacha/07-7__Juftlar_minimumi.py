input()
juftlar = [x for x in map(int, input().split()) if x % 2 == 0]
print(min(juftlar) if juftlar else "No")