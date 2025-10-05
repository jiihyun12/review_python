# 251005

from collections import deque

T = int(input())  

for _ in range(T):
    M, N, K = map(int, input().split())  
    field = [[0] * M for _ in range(N)]  

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1 

    dx = [0, 0, -1, 1]  
    dy = [-1, 1, 0, 0]  

    def bfs(y, x):
        q = deque([(y, x)])
        field[y][x] = 0  
        while q:
            cy, cx = q.popleft()
            for i in range(4):  
                ny, nx = cy + dy[i], cx + dx[i]
   
                if 0 <= ny < N and 0 <= nx < M and field[ny][nx] == 1:
                    field[ny][nx] = 0  
                    q.append((ny, nx))

    cnt = 0  
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:  
                bfs(i, j)         
                cnt += 1          
    print(cnt)

# ----------------------------------

# ------------------------------------------------------------
# BOJ 1012: 유기농 배추 (BFS)
# ------------------------------------------------------------
# 목표:
#   1(배추)들이 상/하/좌/우로 연결된 묶음(= connected component) 개수를 센다.
#   각 묶음마다 지렁이 1마리 필요 → 묶음 개수 = 정답.
#
# 방법(개요):
#   - 밭을 N(행) x M(열) 2차원 배열로 표현 (0: 빈칸, 1: 배추).
#   - 모든 칸을 순회하면서 아직 방문하지 않은 배추(1)를 만나면
#     그 칸을 시작으로 BFS를 돌려 연결된 배추들을 전부 방문 처리(0으로 변경).
#   - BFS를 한 번 돌 때마다 "덩어리 1개"를 처리한 것이므로 카운트를 +1.
#
# 구현 포인트:
#   - 방문표시는 별도 visited 배열 대신 field[y][x]를 1→0으로 바꿔 재사용(메모리/속도/코드 간결).
#   - 입력 좌표는 (x, y) 순서로 주어지지만, 2차원 리스트 인덱싱은 [y][x] 임에 주의.
#   - BFS 큐는 collections.deque 사용 (popleft O(1)).
#   - 4방향 탐색(상/하/좌/우)만 허용, 대각선은 불가.
#
# 복잡도:
#   - 각 칸은 최대 한 번만 큐에 들어가고 방문 처리 → O(N*M).
# ------------------------------------------------------------

from collections import deque

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    # M: 가로(열 개수, x축 길이), N: 세로(행 개수, y축 길이), K: 배추가 심어진 칸의 개수
    M, N, K = map(int, input().split())

    # 배추밭 초기화: N행 x M열, 0으로 채움 (아직 배추 없음)
    field = [[0] * M for _ in range(N)]

    # 배추가 심어진 좌표를 표시
    # 입력은 (x, y)로 주어지므로 field[y][x]에 1을 기록
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    # 상/하/좌/우 이동 벡터
    # dy, dx를 같은 인덱스로 묶어서 사용 (예: i=0 → 위로 한 칸)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(start_y: int, start_x: int) -> None:
        """
        (start_y, start_x)에서 시작해 상하좌우로 연결된 모든 배추(1)를
        방문 처리(0으로 변경)한다. 별도 반환값 없음 — field를 '제자리에서' 바꾼다.
        """

        # BFS 큐에 시작점을 넣기 전에 방문 처리(1→0)하여
        # 같은 칸이 중복해서 큐에 들어가는 것을 방지
        field[start_y][start_x] = 0
        q = deque([(start_y, start_x)])

        # 큐가 빌 때까지 반복 → 같은 덩어리의 모든 배추를 소거
        while q:
            y, x = q.popleft()  # FIFO: 먼저 들어온 좌표부터 꺼내 처리

            # 현재 칸의 4방향 이웃 칸들을 확인
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # (1) 밭 경계를 벗어나면 스킵
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue

                # (2) 배추가 없는 칸(0)이면 스킵
                if field[ny][nx] == 0:
                    continue

                # (3) 배추가 있는 칸(1)을 발견 → 방문 처리 후 큐에 추가
                field[ny][nx] = 0         # 방문 표시: 다시 오지 않도록 0으로 변경
                q.append((ny, nx))        # 이웃 칸을 다음 탐색 대상으로 등록

    # 덩어리(=지렁이 수) 카운터
    count = 0

    # 모든 칸을 훑으며, 아직 방문하지 않은 배추(1)를 시작점으로 BFS 수행
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:  # 새로운 덩어리의 시작점을 찾음
                bfs(y, x)         # 연결된 모든 배추를 한 번에 방문 처리
                count += 1        # BFS 1회 = 덩어리 1개 처리 완료

    # 현재 테스트 케이스의 결과 출력
    print(count)
