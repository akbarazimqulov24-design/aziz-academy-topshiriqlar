n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})

best_user = max(users, key=lambda u: len(u['tags']))
print(best_user['username'])