# 251001

# 1번 컴퓨터가 바이러스에 걸림.
# 네트워크 상에서 직접 or 간접적으로 연결된 모든 컴퓨터가 감염됨
# 감염된 컴퓨터의 총 개수(1번 제외)를 출력

from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

bfs(1)
print(visited.count(True) - 1)


# ==================================

# ------------------------------------------------------------
# BOJ 2606: 바이러스  (BFS 풀이, 상세 주석)
# ------------------------------------------------------------
# [문제 요약]
# - 1번 컴퓨터가 바이러스에 감염됨.
# - 네트워크 상에서 "직접 또는 간접으로" 연결된 모든 컴퓨터가 감염됨.
# - 감염된 컴퓨터 수(1번 제외)를 출력.
#
# [접근 방법]
# - "연결" 관계 → 그래프 문제.
# - 1번 컴퓨터에서 시작하여 연결된 모든 정점을 방문 → BFS(또는 DFS)로 가능.
# - BFS: 큐로 '가까운 것부터' 차례차례 방문. (여기선 방문 순서는 중요하지 않고,
#        총 몇 대가 연결되었는지만 중요)
#
# [구현 포인트]
# - 무방향 그래프: 간선 (a, b)가 주어지면 a의 이웃에 b, b의 이웃에 a 모두 추가.
# - 방문 체크(visited)는 "큐에 넣을 때(True)"로 하여 같은 정점이 큐에 여러 번 들어가는 중복을 방지.
# - 감염 개수는 시작점 1번을 제외해야 하므로, 새롭게 방문하는 이웃을 발견할 때 +1.
#
# [복잡도]
# - 인접 리스트 + BFS → O(N + M)  (N: 컴퓨터 수, M: 연결 수)
# ------------------------------------------------------------

from collections import deque
import sys

# 입력이 많지 않지만, 습관적으로 사용하면 안전/빠름
input = sys.stdin.readline

# 컴퓨터(정점) 수
N = int(input().strip())
# 연결(간선) 수
M = int(input().strip())

# 인접 리스트 (1번부터 N번까지 사용하므로 N+1 크기)
graph = [[] for _ in range(N + 1)]

# 무방향 그래프 연결 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 배열
visited = [False] * (N + 1)

def bfs(start: int) -> int:
    """
    시작 정점(start)에서 BFS로 연결된 모든 정점을 방문하고,
    start를 제외한 '새로 감염된 컴퓨터 수'를 반환한다.
    """
    q = deque()

    # 시작 정점 큐에 넣으면서 바로 방문 처리
    visited[start] = True
    q.append(start)

    infected = 0  # 1번을 제외한 감염된 컴퓨터 수

    while q:
        v = q.popleft()  # 가장 먼저 들어온 정점부터 꺼내 처리 (FIFO)

        # 현재 정점 v와 연결된 모든 이웃들을 확인
        for nxt in graph[v]:
            # 아직 방문하지 않은 이웃만 처리
            if not visited[nxt]:
                visited[nxt] = True   # 큐에 넣는 시점에 방문 처리(중복 삽입 방지)
                infected += 1         # 1번에서 퍼져 방문된 새 이웃 ⇒ 감염 +1
                q.append(nxt)         # 다음에 탐색할 대상으로 큐에 추가

    return infected

# 1번 컴퓨터에서 시작하여 감염된 컴퓨터 수 출력 (1번 제외)
print(bfs(1))
