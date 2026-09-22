import sys

lines = sys.stdin.read().splitlines()
a, b, c, = [set(map(int, line.split())) for line in lines[:3]]
print(*sorted(a & b & c))