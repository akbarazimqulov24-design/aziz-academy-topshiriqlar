lst = input().split()
print("Ha" if len(lst) != len(set(lst)) else "Yoq")