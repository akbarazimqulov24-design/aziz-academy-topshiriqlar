import sys

d = sys.stdin.read().split()
for name, price in sorted(
    zip(d[1::2], map(int, d[2::2])), key=lambda x: x[1]
):
    print(name, price)
