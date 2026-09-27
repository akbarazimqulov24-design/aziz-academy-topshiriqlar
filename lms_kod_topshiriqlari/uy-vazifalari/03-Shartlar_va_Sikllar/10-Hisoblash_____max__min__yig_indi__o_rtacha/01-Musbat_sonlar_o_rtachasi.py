n = int(input())
pos = [x for _ in range(n) if (x := int(input())) > 0]
print(sum(pos) // len(pos) if pos else 0)