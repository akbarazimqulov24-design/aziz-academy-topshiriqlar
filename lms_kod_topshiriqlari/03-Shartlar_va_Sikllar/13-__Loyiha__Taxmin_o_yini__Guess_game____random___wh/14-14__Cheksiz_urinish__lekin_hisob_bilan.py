import sys

for i, line in enumerate(sys.stdin, 1):
    if int(line.strip()) == 11:
        print(i)
        break