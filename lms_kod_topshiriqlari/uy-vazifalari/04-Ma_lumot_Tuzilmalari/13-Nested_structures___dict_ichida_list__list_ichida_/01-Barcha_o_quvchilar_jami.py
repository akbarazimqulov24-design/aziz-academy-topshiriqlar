n = int(input())
total = 0
for _ in range(n):
    total += len(input().split()) - 1
print(total)    