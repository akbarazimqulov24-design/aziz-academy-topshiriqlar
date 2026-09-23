import sys

d = sys.stdin.read().split()
if d:
    n = int(d[0])
    s = set()
    i = 1
    for _ in range(n):
        k = int(d[i + 1])
        s.update(d[i + 2 : i + 2 + k])
        i += 2 + k
    print(len(s))