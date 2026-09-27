from collections import Counter

nums = input().split()
print(Counter(nums).most_common(1)[0][0])