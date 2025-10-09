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

# 하나의 회의실에서 겹치지 않게 최대 몇 개의 회의를 배치할 수 있나

#회의 N개를 (시작, 종료) 튜플로 저장
N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 종료 시간 오름차순으로 정렬.
# 종료 시간이 같다면 시작 시간 오름차순으로 정렬.
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0        # 선택한 회의 개수
end_time = 0   # 마지막으로 선택한 회의의 종료 시각(다음 회의는 이 시각 이상에서 시작해야 함)

for s, e in meetings:
    if s >= end_time:   # 겹치지 않으면(시작이 이전 종료 이상이면) 선택
        cnt += 1
        end_time = e    # 현재 회의의 종료 시각으로 갱신

