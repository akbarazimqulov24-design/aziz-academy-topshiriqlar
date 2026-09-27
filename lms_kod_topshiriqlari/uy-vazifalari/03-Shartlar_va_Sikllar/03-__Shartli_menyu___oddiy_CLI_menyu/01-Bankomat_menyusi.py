cmd = input()
balans = int(input())
summa = int(input())

if cmd == '1':
    print(balans)
elif cmd == '2':
    if summa <= balans:
        print(balans - summa)
    else:
        print("Mablag' yetarli emas")
elif cmd == '3':
    print(balans + summa)
else:
    print("Notogri amal")