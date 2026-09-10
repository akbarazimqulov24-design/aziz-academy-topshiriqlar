import sys

for line in sys.stdin:
    n = int(line.strip())
    print("Correct" if n == 9 else ("Low"  if n < 9 else "High"))
    if n == 9: break