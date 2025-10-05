# 251005

from collections import deque
import sys

input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
    M,N,K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x,y = map(int, input().split())
        field[y][x] = 1

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def bfs(start_y, start_x):
            q = deque()
            q.append((start_y, start_x))
            field[start_y][start_x] = 0

            while q:
                y,x = q.popleft()

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if ny < 0 or ny >= N or nx < 0 or nx >= M:
                        continue

                    if field[ny][nx] == 0:
                        continue

                    field[ny][nx] = 0

                    q.append((ny), (nx))

                    worm_count = 0
                    for y in range(N):
                        for  x in range(M):
                            if field[y],[x] == 1:
                                bfs(y, x)
                                worm_count += 1

                    print(worm_count)