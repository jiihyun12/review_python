# 250921

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

lo, hi = 1, max(arr)

def can_make(L):
    cnt = 0
    for a in arr:
        cnt += a // L
    return cnt >= N

while lo <= hi:
    mid = (lo + hi) // 2
    if can_make(mid):
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)

# =====================================
# 길이 L를 정하면 만들 수 있는 개수 = sum(a // L)
# N개 이상 만들 수 있으면 더 긴 L을 시도, 아니면 더 짧게 → 길이에 대한 이분 탐색
# 정답은 조건을 만족하는 L 중 최대값 → 마지막으로 성공한 hi

# 입력:
# K: 가지고 있는 랜선 개수
# N: 필요한 랜선 개수
# 다음 줄부터 K개의 랜선 길이
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

# 이분 탐색 범위: 자를 길이 L
lo, hi = 1, max(arr)   # 길이는 최소 1, 최대는 가장 긴 랜선 길이

def can_make(L: int) -> bool:
    """길이 L로 잘랐을 때 N개 이상 만들 수 있으면 True"""
    cnt = 0
    for a in arr:
        cnt += a // L  # 각 랜선에서 L 길이로 몇 개 나오는지
    return cnt >= N

# 이분 탐색 (upper bound)
while lo <= hi:
    mid = (lo + hi) // 2  # 시도할 길이
    if can_make(mid):
        # mid 길이로 N개 이상 가능 → 더 길게 시도
        lo = mid + 1
    else:
        # mid 길이로 부족 → 더 짧게
        hi = mid - 1

# hi: 조건을 만족하는 길이 중 최대값
print(hi)
