n = int(input())
for i in range(n):
    row = ['*' if i == j or i + j == n - 1 else '.' for j in range(n)]
    print(''.join(row))