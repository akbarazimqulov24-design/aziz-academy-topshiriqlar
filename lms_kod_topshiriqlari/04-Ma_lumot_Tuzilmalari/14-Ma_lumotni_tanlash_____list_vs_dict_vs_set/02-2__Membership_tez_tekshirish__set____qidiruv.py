n = input()
s = set(map(int, input().split()))
q = int(input())

for _ in range(q):
    x = int(input())
    print("YES" if x in s else "NO")
