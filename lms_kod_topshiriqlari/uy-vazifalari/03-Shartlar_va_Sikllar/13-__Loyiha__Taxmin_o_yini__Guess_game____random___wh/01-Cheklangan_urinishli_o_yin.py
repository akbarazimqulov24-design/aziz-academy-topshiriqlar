target, n = int(input()), int(input())

for _ in range(n):
    guess = int(input())
    if guess == target:
        print("TOPDINGIZ")
        break
    print("KATTA" if guess > target else "KICHIK")
else:
    print("YUTQAZDINGIZ")