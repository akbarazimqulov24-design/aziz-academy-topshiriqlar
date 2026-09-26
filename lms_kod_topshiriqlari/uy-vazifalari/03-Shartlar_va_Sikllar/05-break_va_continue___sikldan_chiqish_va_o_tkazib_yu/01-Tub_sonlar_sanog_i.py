import sys

sanoq = 0
for x in sys.stdin.read().split():
    n = int(x)
    if n == 0: break
    if n < 2: continue
    
    d = 2
    while d * d <= n and n % d != 0: d += 1
    if d * d > n: sanoq += 1
    
print(sanoq)
    