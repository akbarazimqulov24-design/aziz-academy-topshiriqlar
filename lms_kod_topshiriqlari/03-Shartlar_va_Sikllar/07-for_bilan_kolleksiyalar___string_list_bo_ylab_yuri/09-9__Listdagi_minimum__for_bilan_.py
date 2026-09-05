input()
s = list(map(int, input().split()))
k = s[0]
for x in s:
    if x < k:
        k = x
print(k)