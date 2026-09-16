n = int(input())
lst = list(map(int, input().split()))

copied_lst = lst[:]
copied_lst[0] = 99

print(lst)
print(copied_lst)