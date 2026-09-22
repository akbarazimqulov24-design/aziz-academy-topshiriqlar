import sys

data = sys.stdin.read().split()
items, k = data[:-1], int(data[-1])
items.pop(k)
print(*items)