import sys

a = list(map(int, sys.stdin.read().split()))[1:]
print(sum(x > 0 for x in a), sum(x < 0 for x in a))