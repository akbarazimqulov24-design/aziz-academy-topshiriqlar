a = set(input().split())
b = input().split()

print(sum(1 for x in b if x in a))