A = set(input().strip().split())
B = set(input().strip().split())

res = sorted(A & B)

print(len(res))
if res:
    print(*res, sep='\n')
