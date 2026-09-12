import sys

data = sys.stdin.read().split()
if len(data) >= 3:
    a = int(data[0])
    b = int(data[1])
    tanlov = int(data[2])
    
    if tanlov == 6:
        print(a ** b)