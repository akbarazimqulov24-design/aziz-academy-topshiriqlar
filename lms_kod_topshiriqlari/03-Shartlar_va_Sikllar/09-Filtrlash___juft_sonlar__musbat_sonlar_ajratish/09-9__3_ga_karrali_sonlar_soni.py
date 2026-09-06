n = int(input())
sonlar = list(map(int,input().split()))
print(sum(1 for x in sonlar if x % 3 == 0))