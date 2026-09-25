n = int(input())
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7}\n{'-'*12}+-----+{'-'*7}")
for _ in range(n):
    p, q, pr = input().split()
    print(f"{p:<12} | {int(q):>5} | {int(pr):>7}")