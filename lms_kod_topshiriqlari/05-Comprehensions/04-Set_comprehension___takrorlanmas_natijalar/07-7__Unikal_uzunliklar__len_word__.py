words = input().split()
uzunliklar = sorted({len(w) for w in words})
print(*uzunliklar)
