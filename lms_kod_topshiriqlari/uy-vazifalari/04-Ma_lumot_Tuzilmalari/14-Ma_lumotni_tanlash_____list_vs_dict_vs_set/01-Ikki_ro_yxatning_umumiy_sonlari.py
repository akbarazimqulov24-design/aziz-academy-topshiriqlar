a = set(map(int, input().split()))
b = set(map(int, input().split()))

common = sorted(a & b)
print(*common)