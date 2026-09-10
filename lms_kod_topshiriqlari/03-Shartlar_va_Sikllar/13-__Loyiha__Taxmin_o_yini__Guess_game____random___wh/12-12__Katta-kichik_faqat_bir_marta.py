import sys

lines = sys.stdin.read().split()
for i, x in enumerate(lines):
    n = int(x)
    if i == 0:
        print("Low" if n < 8 else ("High" if n > 8 else "Correct"))
    else:
        print("Correct" if n == 8 else "Wrong" )