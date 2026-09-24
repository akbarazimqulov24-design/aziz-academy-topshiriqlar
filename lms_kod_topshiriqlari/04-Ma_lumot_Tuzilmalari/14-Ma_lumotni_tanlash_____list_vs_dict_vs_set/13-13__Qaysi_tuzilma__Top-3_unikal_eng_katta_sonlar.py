import sys

data = list(map(int, sys.stdin.read().split()))
top3 = sorted(set(data), reverse=True)[:3]
print(*top3)
            