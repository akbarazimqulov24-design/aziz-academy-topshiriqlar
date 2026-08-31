c = 0
while (n := int(input())) != 0:
    if n < 2: continue
    t = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            t = False
            break
        i += 1
    if t: c += 1
print(c)