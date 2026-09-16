n = int(input())
sonlar = list(map(int, input().split()))

toq_sonlar = [x for x in sonlar if x % 2 != 0]

print(toq_sonlar)