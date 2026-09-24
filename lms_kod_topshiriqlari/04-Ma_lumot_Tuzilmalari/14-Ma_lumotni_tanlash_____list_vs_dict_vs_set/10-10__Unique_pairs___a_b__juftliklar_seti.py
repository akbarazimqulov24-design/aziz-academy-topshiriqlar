from itertools import product

A = map(int, input().split())
B = map(int, input().split())

pairs = sorted(set(product(A, B)))

print(len(pairs))
for a, b in pairs:
    print(a, b)