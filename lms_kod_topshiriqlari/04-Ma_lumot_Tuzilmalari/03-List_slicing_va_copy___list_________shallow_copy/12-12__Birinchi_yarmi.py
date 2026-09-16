import sys

d = sys.stdin.read().split()
print([int(x) for x in d[1 : int(d[0]) // 2 + 1]])
