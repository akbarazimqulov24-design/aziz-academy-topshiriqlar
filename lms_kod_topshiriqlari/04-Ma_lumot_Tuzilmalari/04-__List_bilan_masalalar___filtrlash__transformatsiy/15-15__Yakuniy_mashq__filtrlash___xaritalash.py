n = int(input())
numbers = map(int, input().split())
result = [x * 2 for x in numbers if x > 0]
print(result)