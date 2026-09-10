import sys

for line in sys.stdin:
    n = int(line.strip())
    if 1 <= n <= 10:
        if n == 6:
            print("Correct")
            break
            
    else:
        print("Invalid")