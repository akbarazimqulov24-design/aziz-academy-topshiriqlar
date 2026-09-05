n = int(input())
print('\n'.join(x for x in input().split() if int(x) % 2 == 0))