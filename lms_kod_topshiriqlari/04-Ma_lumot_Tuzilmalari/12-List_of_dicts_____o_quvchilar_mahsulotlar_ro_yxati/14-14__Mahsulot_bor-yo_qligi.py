import sys

data = sys.stdin.read().split()
print("YES" if data[-1] in data[1:-1:2] else "NO")
