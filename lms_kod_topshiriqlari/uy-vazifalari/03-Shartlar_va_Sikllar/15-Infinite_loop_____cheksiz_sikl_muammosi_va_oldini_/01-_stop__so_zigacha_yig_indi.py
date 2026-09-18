total_sum = 0 

while True:
    line = input().strip()
    if line == "stop":
        break
    total_sum += int(line)
    
print(total_sum)    