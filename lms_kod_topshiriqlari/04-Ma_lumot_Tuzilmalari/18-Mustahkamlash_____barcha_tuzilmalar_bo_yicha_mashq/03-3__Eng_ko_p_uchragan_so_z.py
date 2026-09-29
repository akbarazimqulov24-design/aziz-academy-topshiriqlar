from collections import Counter

words = input().split()
cnt = Counter(words)

print(cnt.most_common(1)[0][0])