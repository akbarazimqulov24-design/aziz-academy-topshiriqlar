a, b, c = map(int, input().split())

def calc(a, b, c):
    return a + b * c

print(calc(a, b, c))
print(calc(a, c=c, b=b))
