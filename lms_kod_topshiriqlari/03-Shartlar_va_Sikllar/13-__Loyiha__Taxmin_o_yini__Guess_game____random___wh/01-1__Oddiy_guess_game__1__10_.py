secret_number = 7

while True:
    try:
        guess = int(input())
    except ValueError:
        break
        
    if guess < secret_number:
        print("Low")
    elif guess > secret_number:
        print("High")
    else:
        print("Correct")
        break