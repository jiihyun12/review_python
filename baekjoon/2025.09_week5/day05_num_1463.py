# 250929

import sys
input = sys.stdin.readline

N = int(input().strip())

dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])

# ==========================

# dp[i] = i를 1로 만드는 최소 연산 횟수

# 항상 후보: dp[i] = dp[i-1] + 1
# i % 2 == 0이면 dp[i] = min(dp[i], dp[i//2] + 1)
# i % 3 == 0이면 dp[i] = min(dp[i], dp[i//3] + 1)
# dp[1] = 0에서 시작해 2..N까지 채우면 dp[N]이 답

import sys
input = sys.stdin.readline

N = int(input().strip())   # 목표 숫자 입력

# dp[i] = i를 1로 만드는 최소 연산 횟수
dp = [0] * (N + 1)

# 1은 이미 1이므로 연산 횟수 0
# dp[1] = 0 이 기본값

for i in range(2, N + 1):
    # 방법 1: i → i-1 (항상 가능)
    dp[i] = dp[i - 1] + 1

    # 방법 2: i가 2로 나누어떨어질 때, i → i//2
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 방법 3: i가 3으로 나누어떨어질 때, i → i//3
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 결과: N을 1로 만드는 최소 연산 횟수
print(dp[N])
