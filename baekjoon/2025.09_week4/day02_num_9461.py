# 250925

import sys

input = sys.stdin.readline
T = int(input().strip())

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    N = int(input().strip())
    print(dp[N])

# ==================================

# 문제
# 파도반 수열(P(N)) 정의:
# P(1) = 1, P(2) = 1, P(3) = 1
# P(4) = 2, P(5) = 2
# P(n) = P(n-1) + P(n-5) (n ≥ 6)
# 주어진 N에 대해 P(N)을 구하는 문제


# 알고리즘
# 1. 모든 질의 N을 먼저 읽어서 최댓값 maxN을 구한다.
# 2. dp[1..maxN]를 만들고, 초기값(1,2,3,4,5번째 항)을 채운다.
# 3. 6부터 maxN까지 dp[i] = dp[i-1] + dp[i-5]로 채운다.
# 4. 각 질의에 대해 dp[N]을 출력한다.


# 정답 해설
# import sys
# input = sys.stdin.readline

# # [문제 요약]
# #  - T개의 질의가 주어짐
# #  - 각 질의에 대해 파도반 수열 P(N)을 출력
# #  - P(1)=P(2)=P(3)=1, P(4)=P(5)=2, P(n)=P(n-1)+P(n-5) (n>=6)

# T = int(input().strip())

# # 질의들을 먼저 모두 읽어 저장
# # 이유:
# #  - 가장 큰 N까지만 DP를 계산하면 불필요한 계산을 줄일 수 있음
# #  - 물론 N의 최대가 100이므로 성능 차이는 미미하지만, 습관적으로 깔끔한 패턴
# queries = [int(input().strip()) for _ in range(T)]

# # 질의 중 최대값
# maxN = max(queries)

# # DP 배열 준비: 인덱스를 '문제 정의 그대로' 1부터 쓰기 위해 maxN+1 크기로 생성
# # 파이썬 리스트는 0-index이므로 dp[0]은 더미(사용하지 않음)
# dp = [0] * (maxN + 1)

# # [초기값 설정]
# #  - 점화식이 n>=6에서만 성립하므로,
# #    그 이전 항들은 문제에서 직접 값이 주어짐 → 그대로 세팅
# #  - maxN이 작을 수 있으니, 범위 체크하며 안전하게 할당
# if maxN >= 1: dp[1] = 1
# if maxN >= 2: dp[2] = 1
# if maxN >= 3: dp[3] = 1
# if maxN >= 4: dp[4] = 2
# if maxN >= 5: dp[5] = 2

# #  - P(n) = P(n-1) + P(n-5) 이므로, 작은 n부터 큰 n 순서로
# #    이전에 계산된 값을 재사용하며 누적 계산 (Bottom-up DP)
# for i in range(6, maxN + 1):
#     dp[i] = dp[i - 1] + dp[i - 5]

# # 미리 계산된 dp에서 바로 꺼내 출력 → O(1)
# out_lines = []
# for n in queries:
#     out_lines.append(str(dp[n]))

# print("\n".join(out_lines))
