n = int(input())
sonlar = list(map(int, input().split()))

kvadratlar = [x ** 2 for x in sonlar]

print(kvadratlar)