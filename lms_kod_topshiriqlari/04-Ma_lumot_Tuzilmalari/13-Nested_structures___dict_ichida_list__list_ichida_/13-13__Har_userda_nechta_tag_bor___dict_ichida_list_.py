import sys

d = sys.stdin.read().split()
if d:
    i = 1
    for _ in range(int(d[0])):
        name = d[i]
        k = int(d[i + 1])
        print(name, k)
        i += 2 + k