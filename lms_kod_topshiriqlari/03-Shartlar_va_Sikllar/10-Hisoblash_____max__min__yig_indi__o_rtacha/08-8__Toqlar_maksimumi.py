input()
toqlar = [x for x in map(int, input().split()) if x % 2 != 0]
print(max(toqlar) if toqlar else "No")