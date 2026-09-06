data = list(map(int, input().split()))
n = data[0]

if n == 0:
    print(0)
else:
    m = data[1] if len(data) > 1 else n
    for _ in range(n):
        print(*(range(1, m + 1)))