input()
s = list(map(int, input().split()))
print(min(set(s), key=lambda x: (-s.count(x), x)))