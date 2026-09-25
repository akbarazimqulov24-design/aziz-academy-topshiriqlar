n = int(input())
grades = {}

for _ in range(n):
    name, grade = input().split()
    grades[name] = grade
    
quarey_name = input()
print(grades[quarey_name])
   
    