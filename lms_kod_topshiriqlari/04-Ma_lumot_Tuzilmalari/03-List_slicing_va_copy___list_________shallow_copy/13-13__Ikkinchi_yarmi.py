import sys

d = sys.stdin.read().split()
n, a = int(d[0]), d[1:]
print([int(x) for x in a[n - n // 2 :]])
