n = int(input())
d = 2
while d * d <= n:
    if n % d == 0:
        print(d)
        while n % d == 0:
            n //= d
            
    d += 1
if n > 1:
    print(n)