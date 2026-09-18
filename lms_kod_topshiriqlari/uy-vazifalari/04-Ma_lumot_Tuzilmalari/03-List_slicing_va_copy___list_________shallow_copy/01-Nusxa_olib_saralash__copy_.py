nums = [int(x) for x in input().split()]
nums_copy = nums[:]
nums_copy.sort()

print(*nums)
print(*nums_copy)