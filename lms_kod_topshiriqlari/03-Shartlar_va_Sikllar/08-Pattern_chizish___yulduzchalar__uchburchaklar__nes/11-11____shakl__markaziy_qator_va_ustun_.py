n = int(input())
for i in range(n):
    print("".join("*" if i == n // 2 or j == n // 2 else "." for j in range(n)))