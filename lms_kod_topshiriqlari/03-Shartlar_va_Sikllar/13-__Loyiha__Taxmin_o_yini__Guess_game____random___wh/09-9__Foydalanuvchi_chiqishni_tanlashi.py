import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        print("Exit")
        break
    elif n == 3:
        print("Correct")
    elif n < 3:
        print("Low")
    else:
        print("High")