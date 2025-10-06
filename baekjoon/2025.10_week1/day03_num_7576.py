# 251002

from collections import deque

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 1:
            queue.append((y, x))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    y, x = queue.popleft()
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        
        if tomatos[ny][nx] == 0:
            tomatos[ny][nx] = tomatos[y][x] + 1  
            queue.append((ny, nx))

days = 0
for row in tomatos:
    for val in row:
        if val == 0: 
            print(-1)
            exit()
        days = max(days, val)

print(days - 1)  


# ========================================

# 1. 익은 토마토(1)의 좌표들을 전부 큐에 넣는다.
# 2. 큐에서 하나씩 꺼내서
#    상, 하, 좌, 우 확인
#    안 익은 토마토(0)이면 익히고(1로 바꾸고) + 큐에 새로 추가
# 3️. 큐가 빌 때까지 반복
# 4️. 마지막에 걸린 날짜(단계 수)가 최소 일수


# M, N = map(int, input().split())

# tomatos = [list(map(int, input().split())) for _ in range(N)]
# -->
# tomatos = []
# for _ in range(N):              # N번 반복 (즉, 줄 수만큼)
#     row = list(map(int, input().split()))  # 한 줄 입력받아서 숫자로 바꿈
#     tomatos.append(row)

# 익은 토마토(1)의 좌표를 전부 큐에 넣는다.
# 큐에서 하나씩 꺼내며 상하좌우 칸을 본다.
# 안 익은 토마토(0)이면 익히고(1로 바꾸고),
# 날짜 +1 을 기록하고,
# 큐에 새로 추가.
# 큐가 빌 때까지 반복.
# 마지막에 남은 안 익은 토마토가 있으면 -1,
# 아니면 최대 날짜 출력.

# BFS 준비
queue = deque()

# 1️. 익은 토마토 좌표를 큐에 전부 넣기
for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 1:
            queue.append((y, x))

# 2️. 상하좌우 방향 정의
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 3️. BFS 시작
while queue:
    y, x = queue.popleft()
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        # 창고 밖이면 무시
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        
        # 안 익은 토마토면 익히기
        if tomatos[ny][nx] == 0:
            tomatos[ny][nx] = tomatos[y][x] + 1  # 날짜 누적
            queue.append((ny, nx))

# 4️. 결과 계산
days = 0
for row in tomatos:
    for val in row:
        if val == 0:  # 안 익은 게 남았으면
            print(-1)
            exit()
        days = max(days, val)

print(days - 1)  # 처음 1부터 시작했으니까 하루 뺌
