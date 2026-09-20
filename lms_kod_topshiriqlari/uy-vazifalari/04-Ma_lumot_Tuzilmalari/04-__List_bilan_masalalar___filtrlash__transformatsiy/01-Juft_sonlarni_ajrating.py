nums = input().split()
evens = [x for x in nums if int(x) % 2 == 0]
print(*evens)