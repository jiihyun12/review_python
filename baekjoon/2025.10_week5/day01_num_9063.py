# 251029

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

x_list = [p[0] for p in points]
y_list = [p[1] for p in points]

width = max(x_list) - min(x_list)
height = max(y_list) - min(y_list)

print(width * height)





