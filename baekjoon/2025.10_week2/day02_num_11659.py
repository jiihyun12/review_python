# 251007

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
summ = [0]

for x in nums:
    summ.append(summ[-1] + x)

for _ in range(M):
    i, j = map(int, input().split())
    print(summ[j] - summ[i - 1])


# ===============================

import sys

# input() 대신 sys.stdin.readline을 쓰는 이유:
# - 백준은 입력이 아주 많을 수 있음(M이 최대 100,000).
# - 기본 input()은 상대적으로 느려서 시간 초과가 날 수 있음.
# - sys.stdin.readline()은 개행 문자('\n')까지 포함해서 빠르게 한 줄을 읽는다.
#   (우리는 .strip()을 안 써도 되는 곳에서는 굳이 안 써도 됨)
input = sys.stdin.readline

# -------------------------------
# 1) 첫 줄 입력: N(숫자 개수), M(질의 개수)
# 예: "5 3" 이 들어오면 N=5, M=3 이 된다.
# map(int, input().split()) : 공백 기준으로 자른 문자열들을 int로 변환한다.
# -------------------------------
N, M = map(int, input().split())

# -------------------------------
# 2) 두 번째 줄 입력: N개의 정수
# 예: "5 4 3 2 1" → [5, 4, 3, 2, 1]
# -------------------------------
nums = list(map(int, input().split()))

# ---------------------------------------------------------
# 3) 누적합(prefix sum) 배열 만들기
#    "i~j 구간의 합"을 곧바로 매번 더하면 느리다 (최악 O(N)씩, M번이면 O(N*M))
#    → 그래서 "처음부터 i까지의 합"을 미리 저장해두면,
#      i~j 합 = prefix[j] - prefix[i-1] 로 O(1)에 구할 수 있다.
#
#    왜 맨 앞에 0을 하나 넣는가?
#    - 문제의 구간 인덱스는 1부터 시작(1-based)한다.
#    - i가 1일 때도 i-1 = 0 인덱스를 안전하게 참조하려고
#      prefix[0] = 0 을 만들어둔다.
#    - 이러면 prefix의 길이는 N+1이 되고,
#      prefix[k] = nums[1] + ... + nums[k] 처럼 해석할 수 있다(1-based 관점).
# ---------------------------------------------------------
summ = [0]  # summ[0] = 0 (아무 것도 더하지 않은 합)

# nums의 값을 왼쪽부터 하나씩 보면서 누적해서 더해
# summ[-1] 은 summ의 "마지막 값"을 뜻한다.
# 처음엔 summ = [0]
# x = 5 → summ.append(0 + 5)  → [0, 5]
# x = 4 → summ.append(5 + 4)  → [0, 5, 9]
# x = 3 → summ.append(9 + 3)  → [0, 5, 9, 12]
# ...
for x in nums:
    summ.append(summ[-1] + x)

# ---------------------------------------------------------
# 4) M개의 질의 처리
#    각 줄에 i, j 가 주어지며 (1 ≤ i ≤ j ≤ N)
#    "i번째 수부터 j번째 수까지의 합"을 출력해야 한다.
#
#    핵심 공식:
#      i~j 합 = summ[j] - summ[i-1]
#
#    왜 성립하나?
#    - summ[j]   = nums[1] + nums[2] + ... + nums[j]
#    - summ[i-1] = nums[1] + nums[2] + ... + nums[i-1]
#    (위 둘의 차) = nums[i] + nums[i+1] + ... + nums[j] (딱 i~j 합!)
# ---------------------------------------------------------
for _ in range(M):
    i, j = map(int, input().split())
    # i가 1이면 i-1=0이 되는데, 우리는 이미 summ[0] = 0 을 만들어놨기 때문에 안전하게 작동한다.
    print(summ[j] - summ[i - 1])

    # (디버깅을 원할 때 참고용) 아래 주석을 풀고 확인해봐도 좋아:
    # print(f"i={i}, j={j}, summ[j]={summ[j]}, summ[i-1]={summ[i-1]}, 구간합={summ[j]-summ[i-1]}")


