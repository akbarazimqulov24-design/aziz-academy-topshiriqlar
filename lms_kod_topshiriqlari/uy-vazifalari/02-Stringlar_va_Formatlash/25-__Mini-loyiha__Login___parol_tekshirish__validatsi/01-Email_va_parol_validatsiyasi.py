email = input()
password = input()

is_valid = ('@' in email and 
           '.' in email and
           8 <= len(password) <= 16 and
           email == email.lower())

print(is_valid)