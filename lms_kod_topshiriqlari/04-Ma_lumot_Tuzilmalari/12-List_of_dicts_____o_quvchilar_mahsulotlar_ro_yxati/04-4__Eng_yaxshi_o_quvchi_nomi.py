n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
    
best_students = max(students, key=lambda s: s['score'])
print(best_students['name'])
