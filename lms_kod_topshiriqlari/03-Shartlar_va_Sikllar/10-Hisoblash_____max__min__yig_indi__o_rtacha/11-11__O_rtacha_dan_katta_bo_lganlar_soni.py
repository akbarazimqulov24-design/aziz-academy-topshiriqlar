input()
s = list(map(int, input().split()))
avg = sum(s) / len(s)
print(sum(1 for x in s if x > avg))