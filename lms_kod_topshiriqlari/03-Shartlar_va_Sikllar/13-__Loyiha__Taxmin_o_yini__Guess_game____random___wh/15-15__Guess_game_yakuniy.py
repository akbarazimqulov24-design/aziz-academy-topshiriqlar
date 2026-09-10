import sys

for i, line in enumerate(sys.stdin, 1):
    n = int(line.strip())
    if not 1 <= n <= 20: print("Invalid"); continue
    print("Correct" if n == 20 else ("Low" if n < 20 else "High"))
    if n == 20: print(i); break