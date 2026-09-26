lst = input().split()
seen = set()

for x in lst:
    if x in seen:
        print(x)
        break
    seen.add(x)
else:
    print("yoq")