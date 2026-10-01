words = input().split()
pairs = sorted({(w.lower(), len(w)) for w in words})

print(len(pairs))
for word, legth in pairs:
    print(f"{word}:{legth}")