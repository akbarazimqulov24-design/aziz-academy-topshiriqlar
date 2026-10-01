a, b = list(map(int, input().split())), list(map(int, input().split()))
print(sorted({x for x in a if x in b}))