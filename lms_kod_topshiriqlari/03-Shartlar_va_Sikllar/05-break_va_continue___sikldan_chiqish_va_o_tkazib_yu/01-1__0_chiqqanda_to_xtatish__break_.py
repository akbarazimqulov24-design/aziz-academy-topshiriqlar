import sys

a = 0
for line in sys.stdin:
    
    n = int(line.strip())
    if n == 0:
        break
    a += n
    
print(a)