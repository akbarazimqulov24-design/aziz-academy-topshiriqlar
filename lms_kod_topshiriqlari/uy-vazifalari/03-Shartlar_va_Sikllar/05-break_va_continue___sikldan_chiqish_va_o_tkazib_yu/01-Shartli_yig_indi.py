s = 0
while (n := int(input())) != 0:
    if n > 100: break
    if n > 0: s += n
print(s)