n = int(input())
groups = {d[0]: d[1:] for _ in range(n) for d in [input().split()]}
target_group, student = input().split()

print("Ha" if student in groups.get(target_group, []) else "Yoq")