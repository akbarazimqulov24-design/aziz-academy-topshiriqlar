words = input().split()
lengths = sorted(list({len(x) for w in w in words}))
print(lengths)