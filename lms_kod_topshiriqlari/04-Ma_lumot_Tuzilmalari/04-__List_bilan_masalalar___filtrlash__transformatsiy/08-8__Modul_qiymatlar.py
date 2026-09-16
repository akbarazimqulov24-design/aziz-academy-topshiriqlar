n = int(input())
sonlar = list(map(int, input().split()))

modullar = [abs(x) for x in sonlar]

print(modullar)
