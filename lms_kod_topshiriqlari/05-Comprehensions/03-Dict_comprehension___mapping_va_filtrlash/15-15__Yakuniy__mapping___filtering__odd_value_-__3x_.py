n = int(input())
data = [input().split() for _ in range(n)]
result = {
    k: int(v) * 3 if int(v) % 2 != 0 else int(v) * 2
    for k, v in data
    if abs(int(v)) >= 2
    
}
print(result)