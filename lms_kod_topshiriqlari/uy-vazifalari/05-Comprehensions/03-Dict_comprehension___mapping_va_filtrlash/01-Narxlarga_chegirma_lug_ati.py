prices = list(map(int, input().split()))

res = {p: p - p // 10 for p in prices if p >= 100}

print(res)