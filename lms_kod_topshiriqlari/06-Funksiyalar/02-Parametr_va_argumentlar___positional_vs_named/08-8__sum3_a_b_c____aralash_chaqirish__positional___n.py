a, b, c = map(int, input().split())

def sum3(a, b, c):
    return a + b + c

print(sum3(a, b, c))
print(sum3(a, b=b, c=c))