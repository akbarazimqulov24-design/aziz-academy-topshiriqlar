n = int(input())
sonlar = list(map(int, input().split()))

katta_sonlar = [x for x in sonlar if x > 10]

print(katta_sonlar)
