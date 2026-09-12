import sys

data = sys.stdin.read().split()

if len(data) >= 2:
    print(data[0] + "\t" + data[1])