n = int(input())
lst = list(map(int, input(). split()))
x = int(input())

print(lst.index(x) if x in lst else -1)