import sys

d = sys.stdin.read().split()
print(min([(d[i], int(d[i + 1])) for i in range(1, len(d), 2)], key=lambda x: x[1])[0])
