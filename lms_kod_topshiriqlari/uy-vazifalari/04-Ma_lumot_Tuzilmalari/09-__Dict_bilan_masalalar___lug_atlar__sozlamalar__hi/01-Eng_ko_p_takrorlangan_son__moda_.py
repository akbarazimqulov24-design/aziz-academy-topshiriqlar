nums = list(map(int, input().split()))
counts = {x: nums.count(x) for x in set(nums)}
max_c = max(counts.values())

print(min(x for x, c in counts.items() if  c == max_c))