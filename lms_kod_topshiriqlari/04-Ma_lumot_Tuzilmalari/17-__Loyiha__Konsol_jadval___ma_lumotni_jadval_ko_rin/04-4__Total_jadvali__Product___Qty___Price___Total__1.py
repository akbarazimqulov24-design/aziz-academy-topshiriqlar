n = int(input())

print(f"{'Product':<13}|{'Qty':>6} |{'Price':>8} |{'Total':>10}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

for _ in range(n):
    p, q, pr = input().split()
    print(f"{p:<13}|{int(q):>6} |{int(pr):>8} |{int(q) * int(pr):>10}")