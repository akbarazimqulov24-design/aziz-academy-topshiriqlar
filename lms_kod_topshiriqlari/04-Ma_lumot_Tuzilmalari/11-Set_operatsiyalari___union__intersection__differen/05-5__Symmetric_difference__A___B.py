a = set(map(int, input().split()))
b = set(map(int, input().split()))

simmetrik_farq = a ^ b

if simmetrik_farq:
    print(*sorted(simmetrik_farq))
else:
    print("BO'SH")