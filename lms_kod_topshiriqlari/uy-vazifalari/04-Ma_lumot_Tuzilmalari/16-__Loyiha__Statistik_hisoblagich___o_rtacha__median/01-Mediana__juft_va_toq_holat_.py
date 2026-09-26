import sys

nums = sorted(map(int, sys.stdin.read().split()))
n = len(nums)
print(nums[n // 2] if n % 2 else (nums[n // 2 - 1] + nums[n // 2]) // 2)