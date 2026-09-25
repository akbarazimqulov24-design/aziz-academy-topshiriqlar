nums = list(map(int, input().split()))
print(min(nums, key=lambda x: (-nums.count(x), x)))