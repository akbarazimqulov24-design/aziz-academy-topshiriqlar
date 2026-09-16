n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.insert(len(lst), x)

print(lst)