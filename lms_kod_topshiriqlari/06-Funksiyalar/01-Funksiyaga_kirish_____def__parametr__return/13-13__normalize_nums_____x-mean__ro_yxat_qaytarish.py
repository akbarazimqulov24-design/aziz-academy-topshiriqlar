def normalize(nums):
    m = sum(nums) / len(nums)
    return [ x - m for x in nums]

nums = list(map(int, input().split()))
print(*[f"{x:.2f}" for x in normalize(nums)])