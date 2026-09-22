import sys

d = sys.stdin.read().split()
st =[{"n": d[i], "s": int(d[i+1])} for i in range(1, int(d[0]) * 2, 2)]
avg = sum(s["s"] for s in st) / len(st)

for s in st:
    if s["s"] > avg:
        print(s["n"])