import sys

a, b = map(set, map(str.split, sys.stdin.read().splitlines()))
print(*(sorted(map(int, a ^ b))))