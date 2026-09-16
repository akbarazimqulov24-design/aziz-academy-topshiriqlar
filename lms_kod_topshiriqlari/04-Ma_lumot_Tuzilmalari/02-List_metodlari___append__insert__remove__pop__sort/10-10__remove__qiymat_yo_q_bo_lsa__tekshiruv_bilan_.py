lst = [1, 2, 3]
x = int(input())

if x in lst:
    print("Removed")
    lst.remove(x)
else:
    print("Not found")
    
print(lst)    
 