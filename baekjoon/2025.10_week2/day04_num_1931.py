# 251009

import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for s, e in meetings:
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)

# ===========================================

