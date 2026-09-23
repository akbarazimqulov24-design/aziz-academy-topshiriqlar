a, b = input().split(), input().split()
print(*(y if y != '-' else x for x, y in zip(a, b)))