# 251004

import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])




# ======================================================

# 정수 n이 주어졌을 때,
# n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 문제