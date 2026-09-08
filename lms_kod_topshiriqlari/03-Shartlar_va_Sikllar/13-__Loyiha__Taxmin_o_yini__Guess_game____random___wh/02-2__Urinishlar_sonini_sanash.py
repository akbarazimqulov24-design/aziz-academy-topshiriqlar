secret_number = 5
attempts = 0

while True:
    try:
        guess = int(input())
    except valueError:
        break
        
    attempts += 1
    if guess == secret_number:
        print(attempts)
        break