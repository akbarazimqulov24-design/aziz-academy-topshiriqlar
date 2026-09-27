n = int(input())
pb = dict(input().split() for _ in range(n))

q = int(input())
for _ in range(q):
    print(pb.get(input(), "topilmadi"))