a, b, c = map(int, input().split())
f = lambda a, b, c: a * 100 + b * 10 + c

print(f(a, b, c))
print(f(c=c, a=a, b=b))
print(f(a=c, b=b, c=a))