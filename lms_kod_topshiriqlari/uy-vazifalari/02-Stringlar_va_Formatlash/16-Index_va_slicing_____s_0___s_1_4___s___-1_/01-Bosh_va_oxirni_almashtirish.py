s = input()
if len(s) >= 2:
    print(s[-1] + s[1:-1] + s[0])
else:
    print(s)