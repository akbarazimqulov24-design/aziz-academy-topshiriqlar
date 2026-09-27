target = int(input())
score = 100

while True:
    guess = int(input())
    if guess == target:
        print("TOPDINGIZ")
        print(f"Ball: {score}")
        break
    elif guess > target:
        print("KATTA")
    else:
        print("KICHIK")
        
    score = max(0, score - 10)    