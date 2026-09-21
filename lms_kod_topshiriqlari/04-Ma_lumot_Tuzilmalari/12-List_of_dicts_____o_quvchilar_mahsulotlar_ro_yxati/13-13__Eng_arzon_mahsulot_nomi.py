import sys

d = sys.stdin.read().split()
print(min(zip(d[1::2], map(int, d[2::2])), key=lambda x: x[1])[0])
