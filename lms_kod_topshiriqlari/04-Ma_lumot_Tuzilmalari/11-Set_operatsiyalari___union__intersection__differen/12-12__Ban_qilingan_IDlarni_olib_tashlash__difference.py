ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()

res = sorted(ids - banned)
print(*res if res else ["BO'SH"])