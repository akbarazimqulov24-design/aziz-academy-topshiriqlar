n = int(input())
for i in range(n):
    print("*" * n if i == 0 or i == n - 1 else "*" + " " * (n - 2) + "*")