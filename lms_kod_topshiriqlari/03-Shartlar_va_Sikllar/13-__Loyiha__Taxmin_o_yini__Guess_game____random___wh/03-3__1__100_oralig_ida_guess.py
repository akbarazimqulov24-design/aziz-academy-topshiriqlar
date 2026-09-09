import sys

for line in sys.stdin:
    n = int(line)
    print("High" if n > 42 else ("Low" if n < 42 else "Correct"))
    if n == 42:
        break