import sys

d = list(map(int, sys.stdin.read().split()))
print([x for x in d[1:] if 0 < x < 100])