# 251015

from collections import deque  # BFS는 큐(queue)를 써서 구현

N, K = map(int, input().split())  # 수빈이 위치 N, 동생 위치 K

# 방문한 위치 기록용 배열 (중복 방지)
# 0~100000 범위의 위치 가능 (문제 조건)
visited = [0] * 100001

# BFS 시작 (큐에는 (현재위치, 이동시간)을 함께 저장)
queue = deque([N])

while queue:
    x = queue.popleft()  # 현재 위치 꺼냄
    
    # 목표(K)에 도착했으면 걸린 시간(visited[x]) 출력 후 종료
    if x == K:
        print(visited[x])
        break
    
    # 이동 가능한 세 가지 경우 탐색
    for nx in (x-1, x+1, x*2):
        # 1) 범위 벗어나면 무시
        if 0 <= nx <= 100000:
            # 2) 아직 방문 안 했으면
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1  # 이전 시간 + 1초
                queue.append(nx)  # 큐에 다음 위치 추가
