login = input()
password = input()

print(len(login) >= 3 and len(password) >= 8 and login != password)