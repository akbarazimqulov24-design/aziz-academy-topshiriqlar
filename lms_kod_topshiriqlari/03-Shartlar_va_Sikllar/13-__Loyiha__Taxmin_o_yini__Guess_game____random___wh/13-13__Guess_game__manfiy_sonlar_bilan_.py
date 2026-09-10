import sys

for line in sys.stdin:
    n = int(line.strip())
    print("Correct" if n == -4 else ("High" if n > -4 else "Low"))
    if n == -4: break