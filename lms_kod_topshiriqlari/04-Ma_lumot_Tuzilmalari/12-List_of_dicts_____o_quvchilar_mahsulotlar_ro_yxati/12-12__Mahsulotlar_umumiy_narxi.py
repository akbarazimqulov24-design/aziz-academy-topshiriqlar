import sys

data = sys.stdin.read().split()
print(sum(int(x) for x in data[2::2]))
