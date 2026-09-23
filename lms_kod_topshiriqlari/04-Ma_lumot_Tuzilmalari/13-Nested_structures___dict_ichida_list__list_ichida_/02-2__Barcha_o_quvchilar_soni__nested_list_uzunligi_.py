n = int(input().strip())
total_students = 0

for _ in range(n):
    parts = input().split()
    if len(parts) > 1:
        k = int(parts[1])
        total_students += k
        
print(total_students)        