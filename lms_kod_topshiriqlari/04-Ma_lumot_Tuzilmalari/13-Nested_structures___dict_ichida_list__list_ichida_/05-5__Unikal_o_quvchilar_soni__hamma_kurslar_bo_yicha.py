import sys

d = sys.stdin.read().split()
s = set()
i = 1

for _ in range(int(d[0])):
    k = int(d[i+1])
    # d[i+2] dan boshlanib qirqib olamiz (d[i+1] dagi k soni tushib qoladi)
    s.update(d[i + 2 : i + 2 + k])
    i += 2 + k
    
print(len(s))