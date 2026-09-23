a = set(map(int, input().split()))
b = set(map(int, input().split()))

farq = a - b

if farq:
    print(*sorted(farq))
else:
    print("BO'SH")