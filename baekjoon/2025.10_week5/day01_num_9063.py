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

# ====================

# 점의 개수 입력
N = int(input())

# 좌표들을 저장할 리스트
points = []

# N개의 점 입력받기
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 각각 x좌표와 y좌표만 따로 뽑기
x_list = [p[0] for p in points]
y_list = [p[1] for p in points]

# 가로와 세로 길이 구하기
width = max(x_list) - min(x_list)
height = max(y_list) - min(y_list)

# 넓이 = 가로 × 세로
print(width * height)




