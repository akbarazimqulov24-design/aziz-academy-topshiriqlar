n = int(input())
s, c = 0, 0

for _ in range(n):
    x = int(input())
    if x > 0:
        s += x
        c += 1
        
print(s // c if c > 0 else 0)