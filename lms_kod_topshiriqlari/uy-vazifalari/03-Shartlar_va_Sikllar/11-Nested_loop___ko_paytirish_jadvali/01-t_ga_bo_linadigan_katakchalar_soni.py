n, t = int(input()), int(input())
print(sum(1 for i in range(1, n + 1) for j in range(1, n + 1) if (i * j) % t == 0))