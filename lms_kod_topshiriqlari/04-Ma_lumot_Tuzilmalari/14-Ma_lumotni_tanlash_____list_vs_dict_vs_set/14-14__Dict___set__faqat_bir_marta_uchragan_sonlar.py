import sys
from collections import Counter

data = list(map(int, sys.stdin.read().split()))
res = sorted(k for k, v in Counter(data).items() if v == 1)

print(*res) if res else print("EMPTY")
