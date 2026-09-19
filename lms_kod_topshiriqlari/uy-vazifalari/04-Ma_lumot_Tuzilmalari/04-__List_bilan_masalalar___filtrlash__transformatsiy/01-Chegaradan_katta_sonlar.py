numbers = list(map(int, input().split()))
t = int(input())

result = [x for x in numbers if x > t]

print(*result)

