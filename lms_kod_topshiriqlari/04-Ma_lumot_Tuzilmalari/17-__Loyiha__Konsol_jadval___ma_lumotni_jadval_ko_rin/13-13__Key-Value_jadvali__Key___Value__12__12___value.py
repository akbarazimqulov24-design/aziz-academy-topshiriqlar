n = int(input())
data = []

for _ in range(n):
    key, value = input().split()
    data.append((key, int(value)))

print("Key          |        Value")
print("------------+------------")

for key, value in data:
    print(f"{key:<12} | {value:>11}")