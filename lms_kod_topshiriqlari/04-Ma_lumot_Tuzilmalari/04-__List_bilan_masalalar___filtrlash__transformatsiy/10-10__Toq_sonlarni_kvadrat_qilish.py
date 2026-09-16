import sys

d = list(map(int, sys.stdin.read().split()))
print([x**2 for x in d[1:] if x % 2])
