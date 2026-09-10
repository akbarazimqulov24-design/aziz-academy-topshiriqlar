import sys

for i, line in enumerate(sys.stdin, 1):
    if int(line.strip()) == 8:
        print("Correct")
        sys.exit()
        
print("Game Over")