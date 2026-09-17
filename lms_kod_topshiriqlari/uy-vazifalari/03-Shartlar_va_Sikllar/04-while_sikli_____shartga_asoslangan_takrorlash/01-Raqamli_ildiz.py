n = int(input())

while n >= 10:
    yigindi = 0
    temp = n
    while temp > 0:
        yigindi += temp % 10
        temp //= 10
    n = yigindi
    
print(n)