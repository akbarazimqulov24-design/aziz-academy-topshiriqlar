n = int(input())
nums = [int(input()) for _ in range(n)]

print(nums.index(max(nums)) + 1)