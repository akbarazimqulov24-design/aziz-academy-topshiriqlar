import statistics

nums = sorted(map(int, input().split()))
print(f"{statistics.median(nums):.2f}")
