s = input()
digits = sorted({ch for ch in s if ch.isdigit()})

if digits:
    print(*digits)
else:
    print("BO'SH")
