def cals_all(a, b, c):
    return (a + b + c, a * b * c, max(a, b, c), min(a, b, c))

a, b, c = map(int, input().split())

print("pos:", *cals_all(a, b, c))
print("named:", *cals_all(c=c, a=a, b=b))