from collections import Counter

nums = input().split()
print(sum(1 for v in Counter(nums).values() if v > 1))
