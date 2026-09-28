t = int(input())
k = int(input())
narx = 4000 if t == 3 else 1700
print(narx if k == 1 else (narx // 2 if k == 2 else 0))