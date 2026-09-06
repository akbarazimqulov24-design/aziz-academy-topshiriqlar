n = int(input())
sonlar = list(map(int, input().split()))

for x in sonlar:
    if x % 5 == 0:
        print(x)