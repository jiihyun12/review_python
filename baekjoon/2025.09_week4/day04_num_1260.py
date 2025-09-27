# 250927

from collections import deque

# -----------------------------
# 입력
# -----------------------------
# N: 정점 수, M: 간선 수, V: 시작 정점
N, M, V = map(int, input().split())

# 인접 리스트(1-index). 각 정점에 연결된 이웃들을 담는다.
graph = [[] for _ in range(N + 1)]

# 무방향 그래프이므로 양쪽에 모두 넣는다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 문제 요구: "항상 번호가 작은 정점부터" 방문해야 한다.
# → 인접 리스트를 오름차순으로 정렬해두면,
#    DFS/BFS 모두에서 작은 번호부터 탐색/방문이 쉬워진다.
for i in range(1, N + 1):
    graph[i].sort()


# -----------------------------
# DFS (스택으로 구현: 재귀 X)
# -----------------------------
def dfs_stack(start: int):
    # visited: 한 번 방문한 정점을 다시 처리하지 않게 막는 용도.
    visited = [False] * (N + 1)
    # 스택 초기화. 스택은 LIFO(후입선출): "마지막에 넣은 것"이 먼저 나온다.
    stack = [start]
    # 방문 순서를 기록할 리스트
    order = []

    # 스택이 빌 때까지 반복
    while stack:
        # pop()으로 "맨 뒤" 원소(가장 최근에 들어간 정점)를 꺼낸다.
        node = stack.pop()

        # 이미 방문했다면 스킵
        if visited[node]:
            continue

        # 방문 처리 + 순서 기록
        visited[node] = True
        order.append(node)

        # 핵심 포인트:
        # - graph[node]는 [작은번호, ..., 큰번호]로 정렬되어 있다.
        # - 스택은 "뒤에 넣은 것이 먼저 pop"되므로,
        #   작은 번호를 "먼저 방문"하려면 "큰 번호부터" 스택에 넣어야 한다.
        #   (큰 것부터 push → 작은 것이 더 나중에 push됨 → 나중에 push된 작은 것이 먼저 pop)
        for nxt in reversed(graph[node]):
            if not visited[nxt]:
                stack.append(nxt)

    return order


# -----------------------------
# BFS (큐로 구현)
# -----------------------------
def bfs_queue(start: int):
    visited = [False] * (N + 1)
    # deque는 양쪽 입출력이 O(1)인 큐. popleft()로 맨 앞을 빠르게 꺼낼 수 있다.
    q = deque([start])
    visited[start] = True  # 큐에 넣을 때 바로 방문 처리(중복 삽입 방지)
    order = []

    # 큐가 빌 때까지 반복
    while q:
        # popleft(): FIFO(선입선출). 먼저 들어간 정점이 먼저 나온다.
        node = q.popleft()
        order.append(node)

        # 작은 번호부터 방문해야 하므로 graph[node]는 이미 정렬되어 있음.
        # 방문하지 않은 이웃들을 큐의 "뒤"에 차례로 넣는다.
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True  # 큐에 넣는 순간 방문 표시 (중복 삽입 방지)
                q.append(nxt)

    return order


# -----------------------------
# 실행 및 출력
# -----------------------------
# DFS 방문 순서: 공백 구분으로 한 줄 출력
print(*dfs_stack(V))
# BFS 방문 순서: 공백 구분으로 한 줄 출력
print(*bfs_queue(V))


# =================================
# 정렬: “작은 번호부터 방문” 조건을 맞추기 위해 각 인접 리스트를 오름차순 정렬

# DFS=스택: 재귀 대신 스택(LIFO) 사용. “작은 번호부터”를 맞추려면 큰 번호부터 push → 작은 번호가 먼저 pop

# BFS=큐: 가까운 정점부터 차례대로 방문해야 하므로 FIFO 큐 사용(deque + popleft())

# visited 타이밍
# DFS: 꺼내서 처리할 때 방문 표시(스택 특성상 중복 넣어도 pop 시 필터링).
# BFS: 큐에 넣을 때 즉시 방문 표시(같은 정점이 큐에 여러 번 들어가는 걸 방지).

# ===========================================
# DFS → 스택 (깊게 먼저)
# BFS → 큐 (넓게 차례대로)

# 큐(Queue)
# 먼저 들어온 데이터가 먼저 나감 (FIFO, First In First Out)
# 예시: 은행 창구 줄 서기 → 먼저 선 사람부터 처리
# 파이썬에선 collections.deque.append() + collections.deque.popleft()

# 스택(Stack)
# 먼저 들어온 게 나중에 나감 (LIFO)
# 예시: 접시 쌓아둔 거 → 맨 위 접시부터 꺼냄
# 파이썬에선 list.append() + list.pop()