while (s := input()) != "0":
    a, b = map(int, s.split())
    t, c = int(input()), a + b
    if t == 2: c = a - b
    elif t == 3: c = a * b
    elif t == 4: c = a / b
    print(c)
print("Exit")

