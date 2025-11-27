# 251127

import sys

N = int(sys.stdin.readline().strip())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort(key=lambda p: (p[0], p[1]))

for x, y in points:
    print(x, y)

# ==============================

# 각 점을 (x, y) 튜플로 리스트에 저장
# sort()에 key를 줘서 (x, y) 기준으로 정렬

# 파이썬에서 튜플은 앞에서부터 차례대로 비교하니까
# (x, y)로 정렬하면 자동으로
# x 먼저 비교 --> 같으면 y 비교


##
#sys.stdin.readline() 쓰는 이유:
# N이 최대 100,000까지라서, input()보다 빠르게 하려고

# points.sort(key=lambda p: (p[0], p[1]))
# 그냥 points.sort()만 써도 같은 효과지만,
# 기준을 명시해두면 보기 더 좋음.