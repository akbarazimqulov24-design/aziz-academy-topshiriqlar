n = int(input())
total = 0
i = 0

while i < n:
    num = int(input())
    i += 1
    if num <= 0:
        continue
    total += num
    
print(total)