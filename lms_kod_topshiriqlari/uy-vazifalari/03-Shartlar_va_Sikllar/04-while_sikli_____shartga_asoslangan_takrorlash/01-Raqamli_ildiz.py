n = input()

while len(n) > 1:
    yigindi = 0
    for x in n:
        yigindi += int(x)
    n = str(yigindi)
    
print(n)