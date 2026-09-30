n = int(input())
data = [input().split() for _ in range(n)]
result = {k: "even" if int(v) % 2 == 0 else "odd" for k, v in data}
print(result)