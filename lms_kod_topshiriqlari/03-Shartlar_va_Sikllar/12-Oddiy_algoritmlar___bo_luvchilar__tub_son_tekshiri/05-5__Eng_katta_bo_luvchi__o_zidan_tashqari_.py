n = int(input())

topildi = 0
for i in range(n - 1, 0, -1):
    if n % i == 0:
        topildi = i
        break
        
print(topildi)