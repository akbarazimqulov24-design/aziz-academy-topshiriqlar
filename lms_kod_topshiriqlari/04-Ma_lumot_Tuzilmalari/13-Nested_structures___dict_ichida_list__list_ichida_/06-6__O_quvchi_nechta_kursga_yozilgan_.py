import sys

d = sys.stdin.read().split()
target, idx, count = d[-1], 1, 0

for _ in range(int(d[0])):
    k = int(d[idx + 1])
    if target in d[idx + 2 : idx + 2 + k]:
        count += 1
    idx += 2 + k
    
print(count)