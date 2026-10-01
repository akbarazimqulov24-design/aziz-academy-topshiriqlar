words = input().split()
palindromes = sorted({w.lower() for w in words if w.lower() == w.lower()[::-1]})

if palindromes:
    print(*palindromes)
else:
    print("BO'SH")