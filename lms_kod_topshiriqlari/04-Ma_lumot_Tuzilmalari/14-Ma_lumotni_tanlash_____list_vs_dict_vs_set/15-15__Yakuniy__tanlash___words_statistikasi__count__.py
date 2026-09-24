from collections import Counter

words = input().lower().split()
counts = Counter(words)

top_word, top_count = min(counts.items(), key=lambda x: (-x[1], x[0]))

print(f"total: {len(words)}")
print(f"unique: {len(counts)}")
print(f"top: {top_word} {top_count}")