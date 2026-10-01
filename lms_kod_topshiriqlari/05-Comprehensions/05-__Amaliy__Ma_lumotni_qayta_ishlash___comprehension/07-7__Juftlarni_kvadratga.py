sonlar = list(map(int, input().split()))
natija = [x**2 for x in sonlar if x % 2 == 0]
print(natija)