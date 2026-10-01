x, y, z = map(int, input().split())

def ordet3(a, b, c):
    return f"a={a} b={b} c={c}"

print(ordet3(x, y, z))
print(ordet3(c=x, b=y, a=z))
