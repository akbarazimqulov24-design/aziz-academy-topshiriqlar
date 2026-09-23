n = int(input())
users = [input().split() for _ in range(n)]
print(max(users, key= lambda x: int(x[1]))[0])