t = int(input())
k = int(input())

if t in (1, 2):
    narx = 1700
elif t == 3:
    narx = 4000
else:
    exit(print("Notogri transport"))
    
if k == 1:
    print(narx)
elif k == 2:
    print(narx // 2)
elif k == 3:
    print(0)
else:
    print("Notogri toifa")