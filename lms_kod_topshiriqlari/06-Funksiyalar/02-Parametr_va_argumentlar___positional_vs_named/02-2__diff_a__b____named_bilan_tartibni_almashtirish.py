a, b = map(int, input().split())

def diff(a, b):
    return a - b

print(diff(a, b))
print(diff(b=a, a=b))