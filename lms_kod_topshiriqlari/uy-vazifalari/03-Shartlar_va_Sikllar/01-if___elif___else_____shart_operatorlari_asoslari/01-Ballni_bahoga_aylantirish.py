score = int(input())

if score < 0 or score > 100:
    print("notogri")
elif 86 <= score <= 100:
    print(5)
elif 71 <= score <= 85:
    print(4)
elif 56 <= score <= 70:
    print(3)
else:
    print(2)