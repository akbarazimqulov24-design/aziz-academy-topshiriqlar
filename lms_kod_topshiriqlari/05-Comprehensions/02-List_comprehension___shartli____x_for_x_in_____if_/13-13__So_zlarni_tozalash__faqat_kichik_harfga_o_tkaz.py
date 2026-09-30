words = input().split()
res = [w.lower() for w in words if w.lower().startswith('a')]
print(*res if res else ["BO'SH"])