words = input().split()
counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1
    
for word, count in counts.items():
    print(word, count)