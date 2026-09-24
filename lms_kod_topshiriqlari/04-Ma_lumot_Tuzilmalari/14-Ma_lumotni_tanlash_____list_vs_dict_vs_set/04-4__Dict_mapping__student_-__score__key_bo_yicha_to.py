n = int(input())
scores = dict(input().split() for _ in range(n))
q = int(input())
for _ in range(q):
    print(scores.get(input(), "NOT_FOUND"))
