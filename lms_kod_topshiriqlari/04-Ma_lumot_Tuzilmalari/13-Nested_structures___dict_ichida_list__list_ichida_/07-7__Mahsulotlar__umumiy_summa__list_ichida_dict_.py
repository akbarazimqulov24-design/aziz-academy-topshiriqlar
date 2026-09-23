n = int(input().strip())
print(sum(int(p) * int(q) for _ in range(n) for _, p, q in [input().split()]))