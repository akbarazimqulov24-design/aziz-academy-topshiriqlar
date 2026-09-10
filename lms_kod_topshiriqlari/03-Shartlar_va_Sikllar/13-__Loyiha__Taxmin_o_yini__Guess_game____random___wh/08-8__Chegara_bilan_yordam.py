import sys

for line in sys.stdin:
    d = int(line.strip()) - 15
    print("Correct" if d == 0 else ("Far" if abs(d) >= 5 else "Close"))