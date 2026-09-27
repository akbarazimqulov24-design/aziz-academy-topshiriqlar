items = input().split()
d = {}

for x in items:
    d[x] = d.get(x, 0) + 1
    
# Eng ko'p uchragan va birinchi ko'ringan qiymatni topamizprint
max_val = items[0]
max_count = d[max_val]

for x in d:
    if d[x] > max_count:
        max_count = d[x]
        max_val = x
        
print(max_val)        