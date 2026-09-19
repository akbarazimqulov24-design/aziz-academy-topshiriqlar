s = input().strip()
for k in sorted(set(s)):
    print(f"{k}={s.count(k)}")