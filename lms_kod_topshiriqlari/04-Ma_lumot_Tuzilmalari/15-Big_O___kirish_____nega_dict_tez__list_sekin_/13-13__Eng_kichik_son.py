import sys

data = list(map(int, sys.stdin.read().split()))
if data:
    print(min(data[1:]))
