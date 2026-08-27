import sys

a = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n < 0:
        break
    a += 1
    
print(a)