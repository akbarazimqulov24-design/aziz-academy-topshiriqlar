s = input().lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
res = sorted({ch for ch in s if ch in vowels})

if res:
    print(*res)
else:
    print("BO'SH")
