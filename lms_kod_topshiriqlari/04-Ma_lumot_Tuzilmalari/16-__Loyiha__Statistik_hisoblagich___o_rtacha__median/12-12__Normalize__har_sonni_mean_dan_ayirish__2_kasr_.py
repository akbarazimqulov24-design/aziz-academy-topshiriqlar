a = list(map(int, input().split()))
m = sum(a) / len(a)
print(*(f"{x - m:.2f}" for x in a))
