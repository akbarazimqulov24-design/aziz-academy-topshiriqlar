n = int(input())
students = [{"name": (d := input().split())[0], "age": int(d[1])} for _ in range(n)]

print(max(students, key=lambda s: s["age"])["name"])