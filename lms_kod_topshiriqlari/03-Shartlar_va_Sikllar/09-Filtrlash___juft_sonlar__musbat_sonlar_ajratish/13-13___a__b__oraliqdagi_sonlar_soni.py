n = int(input())
sonlar = list(map(int, input().split()))
a, b = map(int, input().split())
print(sum(1 for x in sonlar if a <= x <= b))