# 250817

# N개의 바구니(1번부터 N번까지)와 M번의 작업이 주어진다.
# 각 작업은 i j k 형태로 주어지며, 이는 i번 바구니부터 j번 바구니까지에 공 번호 k를 넣는다는 의미
# 처음에는 모든 바구니가 비어있음(0)
# 마지막에 각 바구니에 들어있는 공의 번호를 출력하면 된다.

N, M = map(int, input().split())
basket = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        basket[x] = k

print(*basket[1:])

# =========================================

import sys
input = sys.stdin.readline

# N: 바구니 개수, M: 작업 횟수
N, M = map(int, input().split())
baskets = [0] * N  # 1~N 바구니를 0~N-1 인덱스로 보관

for _ in range(M):
    i, j, k = map(int, input().split())
    # 문제는 1-index 구간 [i, j] 이므로 0-index로 변환 -> [i-1, j-1]
    for x in range(i - 1, j):
        baskets[x] = k

# 공백으로 출력
print(*baskets)

# --------------------------------------

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# baskets = [0] * N

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     # 슬라이싱 대입: 길이가 (j-i+1)인 리스트로 한 번에 채우기
#     baskets[i - 1 : j] = [k] * (j - i + 1)

# print(*baskets)

