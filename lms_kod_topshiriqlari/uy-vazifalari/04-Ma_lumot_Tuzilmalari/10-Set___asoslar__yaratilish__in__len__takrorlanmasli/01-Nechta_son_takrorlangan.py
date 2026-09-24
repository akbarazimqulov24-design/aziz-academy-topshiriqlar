seen, dups = set(), set()
for x in input().split():
    dups.add(x) if x in seen else seen.add(x)
print(len(dups))    