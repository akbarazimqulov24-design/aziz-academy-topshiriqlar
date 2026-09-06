n, m = map(int, input().split())
for j in range(1, m + 1):
    print(sum(i * j for i in range(1, n + 1)))