# 250925

import sys
input = sys.stdin.readline

n = int(input().strip())
score = [int(input().strip()) for _ in range(n)]

if n == 1:
    print(score[0])
    exit(0)
elif n == 2:
    print(score[0] + score[1])
    exit(0)
elif n == 3:
    print(max(score[0] + score[2], score[1] + score[2]))
    exit(0)

dp = [0] * n
dp[0] = score[0]                     
dp[1] = score[0] + score[1]         
dp[2] = max(score[0] + score[2],     
            score[1] + score[2])     

for i in range(3, n):
    dp[i] = max(dp[i-2] + score[i],
                dp[i-3] + score[i-1] + score[i])

print(dp[n-1])


# 연속 3계단을 밟을 수 없다는 제약 하에 마지막 계단을 반드시 밟으면서 점수 합의 최댓값을 구하는 문제

# 한 번에 1칸 또는 2칸 오를 수 있음.

# 연속 3칸 금지 → 마지막 계단 i에 도달하는 방법은 둘뿐:

# 1.
# i-2 → i (i-1을 밟지 않음)
# → 최댓값: dp[i-2] + score[i]

# 2.
# i-3 → i-1 → i (i-1을 밟고 오지만, i-2는 건너뜀)
# → 최댓값: dp[i-3] + score[i-1] + score[i]

# import sys
# input = sys.stdin.readline

# n = int(input().strip())
# score = [int(input().strip()) for _ in range(n)]

# # 예외/기저 처리: 계단 수가 1~3일 때는 직접 계산하는 게 안전
# if n == 1:
#     print(score[0])
#     exit(0)
# elif n == 2:
#     print(score[0] + score[1])
#     exit(0)
# elif n == 3:
#     # 세 번째에 도달하려면 (0→2) 또는 (1→2) 둘 중 큰 값
#     # 0→1→2는 연속 3계단이라 불가
#     print(max(score[0] + score[2], score[1] + score[2]))
#     exit(0)

# # dp[i] = i번째(0-index) 계단을 '밟고' 도달했을 때 얻을 수 있는 최댓값
# dp = [0] * n
# dp[0] = score[0]                     # 첫 칸만 밟음
# dp[1] = score[0] + score[1]          # 0→1 (연속 2칸까지는 가능)
# dp[2] = max(score[0] + score[2],     # 0→2
#             score[1] + score[2])     # 1→2  (0→1→2는 연속 3칸이라 불가)

# # 점화식
# for i in range(3, n):
#     # 1) i-2에서 한 번에 2칸 점프해 i로
#     # 2) i-3에서 i-1을 밟고 i로 (i-2는 건너뛰어 연속 3칸 방지)
#     dp[i] = max(dp[i-2] + score[i],
#                 dp[i-3] + score[i-1] + score[i])

# print(dp[n-1])
