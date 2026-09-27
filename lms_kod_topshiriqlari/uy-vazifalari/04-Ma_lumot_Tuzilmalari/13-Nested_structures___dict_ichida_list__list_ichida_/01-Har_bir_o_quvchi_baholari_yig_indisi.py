n = int(input())
students = [{"name": (d := input().split())[0], "grades": list(map(int, d[1:]))} for _ in range(n)]

for s in students:
    print(s["name"], sum(s["grades"]))