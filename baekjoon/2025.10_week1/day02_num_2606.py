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
