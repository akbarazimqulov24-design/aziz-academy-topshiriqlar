res = {}
for _ in range(int(input())):
    g, s = input().split()
    res[g] = res.get(g, 0) + int(s)
    
for g in sorted(res):
    print(g, res[g])