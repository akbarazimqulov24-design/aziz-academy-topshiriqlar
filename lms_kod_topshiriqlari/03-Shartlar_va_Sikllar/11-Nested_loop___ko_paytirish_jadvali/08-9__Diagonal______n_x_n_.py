n = int(input())
for i in range(n):
    row = ['.' if i != j else '*' for j in range(n)]
    print(''.join(row))