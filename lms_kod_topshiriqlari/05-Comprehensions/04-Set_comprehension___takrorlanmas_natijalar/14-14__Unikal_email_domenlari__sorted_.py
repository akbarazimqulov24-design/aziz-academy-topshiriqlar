emails = input().split()
domains = sorted({e.split('@')[1].lower() for e in emails if '@' in e})

if domains:
    print(*domains)
else:
    print("BO'SH")