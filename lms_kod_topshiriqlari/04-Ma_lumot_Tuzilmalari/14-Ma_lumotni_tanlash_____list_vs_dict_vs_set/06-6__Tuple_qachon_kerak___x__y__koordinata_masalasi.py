points = [tuple(map(int, input().split())) for _ in range(int(input()))]
x, y = min(points, key=lambda p: (-p[0], p[1]))
print(x, y)