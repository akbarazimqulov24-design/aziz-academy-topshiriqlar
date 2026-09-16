n = int(input())
lst = list(map(int, input().split()))
x = int(input())

copied_lst = list(lst)
copied_lst.append(x)

print(lst)
print(copied_lst)