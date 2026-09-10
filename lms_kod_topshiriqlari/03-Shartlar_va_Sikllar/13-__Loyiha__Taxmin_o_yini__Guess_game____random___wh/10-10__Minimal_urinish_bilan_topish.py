import sys

for i, line in enumerate(sys.stdin, 1):
    if int(line.strip()) == 1:
        print("Correct")
        print(i)
        break
    print("Try again")