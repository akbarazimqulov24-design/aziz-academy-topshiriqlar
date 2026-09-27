n = int(input())
d = {}

for _ in range(n):
    ism, baho = input().split()
    d[ism] = int(baho)

best = min(d.items(), key=lambda x: (-x[1], x[0]))

print(best[0], best[1])