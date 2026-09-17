def calc(a, b):
    return a + b, a * b

x, y = map(int, input().split())
res1, res2 = calc(x, y)
print(res1)
print(res2)