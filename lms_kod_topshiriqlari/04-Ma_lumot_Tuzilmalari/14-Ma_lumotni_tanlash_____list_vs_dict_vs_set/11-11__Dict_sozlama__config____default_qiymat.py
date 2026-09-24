import sys

data = sys.stdin.read().split()
if data:
    k = int(data[0])
    config = dict(zip(data[1:2*k+1:2], map(int, data[2:2*k+1:2])))
    
q_start = 2 * k + 2
for key in data[q_start:]:
    print(config.get(key, 0))