n = int(input())
m = int(input())
for _ in range(n - 1):
    x = int(input())
    if x > m:
        m = x
print(m)