import sys

lines = sys.stdin.read().splitlines()
if lines:
    n = int(lines[0])
    g = {l.split()[0]: len(l.split()[1:]) for l in lines[1:n+1] if l.split()}
    print(max(g, key=g.get))