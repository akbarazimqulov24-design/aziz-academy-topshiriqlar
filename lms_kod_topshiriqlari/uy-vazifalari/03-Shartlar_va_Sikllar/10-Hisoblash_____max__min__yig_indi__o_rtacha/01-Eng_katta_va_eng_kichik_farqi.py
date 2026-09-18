n = int(input())

first_num = int(input())
mx = first_num
mn = first_num

for _ in range(n - 1):
    num = int(input())
    if num > mx:
        mx = num
    if num < mn:
        mn = num
        
print(mx - mn)        