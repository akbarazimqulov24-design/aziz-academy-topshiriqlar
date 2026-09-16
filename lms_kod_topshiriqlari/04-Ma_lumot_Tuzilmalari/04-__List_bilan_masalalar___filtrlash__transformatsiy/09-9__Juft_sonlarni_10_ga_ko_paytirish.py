n = int(input())
sonlar = list(map(int, input().split()))

natija = [x * 10 for x in sonlar if x % 2 == 0]

print(natija)