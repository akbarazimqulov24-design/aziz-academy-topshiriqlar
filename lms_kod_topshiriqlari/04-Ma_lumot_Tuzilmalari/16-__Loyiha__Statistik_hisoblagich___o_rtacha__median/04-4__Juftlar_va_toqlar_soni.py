s = list(map(int, input().split()))
j = sum(1 for x in s if x % 2 == 0)
print(j, len(s) - j, sep="\n")
