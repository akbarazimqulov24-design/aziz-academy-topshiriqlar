def format_point(x, y):
    return f"({x},{y})"

x, y = map(int, input().split())

res1 = format_point(x, y)
res2 = format_point(y=y, x=x)

print(res1)
print(res2)
