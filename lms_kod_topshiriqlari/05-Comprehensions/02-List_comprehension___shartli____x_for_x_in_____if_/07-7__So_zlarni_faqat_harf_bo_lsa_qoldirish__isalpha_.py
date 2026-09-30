s = input().split()
res = [x for x in s if x.isalpha()]

if res:
    print(" ".join(res))
else:
    print("BO'SH")
