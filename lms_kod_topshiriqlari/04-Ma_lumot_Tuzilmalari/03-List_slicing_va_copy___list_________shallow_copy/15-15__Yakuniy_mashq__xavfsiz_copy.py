import sys

d = sys.stdin.read().split()
if d:
    a = [int(x) for x in d[1:]]
    b = a.copy()
    b.reverse()
    
    print(a)
    print(b)
