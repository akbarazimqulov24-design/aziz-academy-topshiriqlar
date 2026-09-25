n = int(input())
d = {}

for _ in range(n):
    item, count =input().split()
    d[item] = int(count)
    
key = input()
print(d.get(key, "Topilmadi"))