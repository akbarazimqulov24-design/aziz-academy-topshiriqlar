import sys

d = sys.stdin.read().split()
print([int(x) for x in d[1:]][::2])