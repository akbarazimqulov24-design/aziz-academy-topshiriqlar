n = int(input())
students = []

for _ in range(n):
    name, age = input().split()
    students.append({"ism": name, "yosh": int(age)})
for students in students:
    print(students['ism'])