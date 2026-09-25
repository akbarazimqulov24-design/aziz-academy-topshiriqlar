a = list(map(int, input().split()))
r, m = max(a) - min(a), sum(a) / len(a)
print(*(f"{(x - m) / r:.2f}" if r else "0.00" for x in a))
