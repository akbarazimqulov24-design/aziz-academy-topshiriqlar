list1 = input().split()
list2 = set(input().split())

result = []
for x in list1:
    if x in list2 and x not in result:
        result.append(x)
        
print(*(result))        