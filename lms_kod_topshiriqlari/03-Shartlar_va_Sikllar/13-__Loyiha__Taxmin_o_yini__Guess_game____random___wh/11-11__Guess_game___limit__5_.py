import sys

for line in sys.stdin:
    if int(line.strip()) == 10:
        print("Correct")
        sys.exit()
print("You lost")