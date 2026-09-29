n = int(input())

total = 0
for _ in range(n):
    price = int(input())
    count = int(input())
    total += price * count
    
print(total)    