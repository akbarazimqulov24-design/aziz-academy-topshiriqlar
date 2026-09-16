import sys

d = sys.stdin.read().split()
if d:
    n = int(d[0])
    words = d[1:]
    print([x for x in words if len(x) >=n])

