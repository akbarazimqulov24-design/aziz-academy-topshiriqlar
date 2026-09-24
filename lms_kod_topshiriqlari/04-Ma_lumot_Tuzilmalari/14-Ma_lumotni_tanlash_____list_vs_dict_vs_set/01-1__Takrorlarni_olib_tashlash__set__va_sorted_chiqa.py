sonlar = list(map(int, input().split()))
unikal = sorted(set(sonlar))
print(*unikal)
