numbers = list(map(int, input().split()))
print(*(x * 2 for x in numbers))