# 250920

from collections import deque

N, M = map(int, input().split())  
maze = [list(map(int, input().strip())) for _ in range(N)]  

def bfs(x, y):
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1]  

    q = deque()
    q.append((x, y))  

    while q:
        x, y = q.popleft()  

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  
                q.append((nx, ny))             

    return maze[N-1][M-1]

print(bfs(0, 0))


# ==============================================
# 설명

# 1(길)만 따라 시작(1,1) → 도착(N,M) 까지의 최단 거리를 구하는 문제
# 최단 거리는 BFS(너비 우선 탐색) 로 구한다.
# --> DFS(깊이우선탐색) → 끝까지 가봐야 최단인지 알 수 없음 
# BFS는 가까운 칸부터 탐색하므로, 처음 도착하는 순간이 무조건 최단 거리

# 미로가 주어진다.
# 1--> 길, 0--> 벽
# 시작: (1,1) --> 코드에서는 (0,0)
# 끝: (N,M) --> 코드에서는 (N-1, M-1)
# 규칙: 한 번에 상.하.좌.우 한 칸 이동 가능


# 입력 받기
# N, M 읽기 → 미로 크기
# 문자열로 들어오는 101111 같은 줄을 숫자 리스트로 바꿔서 저장

# BFS 시작
# 시작점 (0,0) 큐에 넣음
# maze[0][0] = 1 → 시작 거리는 1칸

# 큐에서 꺼내면서 네 방향 탐색
# 위, 아래, 왼쪽, 오른쪽 좌표 계산
# 범위 벗어나면 건너뜀
# 벽(0)이면 건너뜀
# 길(1)이면 → “처음 방문”이니까 현재 칸 거리 +1 로 바꾸고 큐에 넣음

# 반복
# 큐가 빌 때까지 반복
# 도착점 (N-1,M-1)에 도착하면 그 칸에 적힌 값이 최단 거리


# ====================================================
# 코드 해석

# from collections import deque

# # 1. 입력 받기
# N, M = map(int, input().split())   # N: 행, M: 열
# maze = [list(map(int, input().strip())) for _ in range(N)]  # 미로 입력

# # 2. BFS 함수 정의
# def bfs(x, y):
#     # 상, 하, 좌, 우 이동을 위한 좌표 변화값
#     dx = [-1, 1, 0, 0]  # 행 이동
#     dy = [0, 0, -1, 1]  # 열 이동

#     # 큐 생성
#     q = deque()
#     q.append((x, y))  # 시작점 넣기

#     # BFS 실행
#     while q:
#         x, y = q.popleft()  # 현재 좌표 꺼내기

#         # 네 방향 탐색
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 1) 범위 밖이면 무시
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             # 2) 벽(0)이면 무시
#             if maze[nx][ny] == 0:
#                 continue
#             # 3) 처음 방문하는 길(1)이라면
#             if maze[nx][ny] == 1:
#                 maze[nx][ny] = maze[x][y] + 1  # 현재 거리 + 1
#                 q.append((nx, ny))             # 다음 탐색할 좌표로 추가

#     # 도착 지점에 적힌 숫자가 최단 거리
#     return maze[N-1][M-1]

# # 3. 결과 출력
# print(bfs(0, 0))
