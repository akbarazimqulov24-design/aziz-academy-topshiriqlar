n, m = map(int, input().split())
print(*(j**2 for j in range(2, m + 1)))