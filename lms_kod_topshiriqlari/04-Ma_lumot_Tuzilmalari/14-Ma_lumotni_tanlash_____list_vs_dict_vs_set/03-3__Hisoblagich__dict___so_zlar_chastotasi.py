from collections import Counter

for k, v in sorted(Counter(input().lower().split()).items()):
    print(k, v)

