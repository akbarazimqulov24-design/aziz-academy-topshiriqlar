n = int(input())

max_val = None
max_pos = -1

for i in range(1, n + 1):
    num = int(input())
    if max_val is None or num > max_val:
        max_val = num
        max_pos = i
        
print(max_pos)