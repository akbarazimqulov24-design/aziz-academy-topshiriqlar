import sys

data = sys.stdin.read().splitlines()
if data:
    nums, t = list(map(int, data[0].split())), int(data[1])
    s = set()
    print("Ha" if any(t - x in s or s.add(x) for x in nums) else "Yoq")