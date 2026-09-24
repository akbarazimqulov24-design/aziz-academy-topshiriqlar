s = input()
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1
    
for char, count in d.items():
    print(char, count)