n = int(input())
numbers = list(map(int, input().split()))

max_val = numbers[0]
for x in numbers:
    if x > max_val:
        max_val = x
        
print(max_val)