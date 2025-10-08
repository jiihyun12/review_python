# 250930

# 집합(set) 으로 듣도 못한 사람/보도 못한 사람을 받아서 교집합을 정렬해 출력

import sys
input = sys.stdin.readline

N,M = map(int, input().split())

heard = {input().strip() for _ in range(N)}
seen = {input().strip() for _ in range(M)}

both = sorted(heard & seen)

print(len(both))
print("\n".join(both))

# ============================

# sys.stdin.readline 사용: 입력 줄 수가 많을 때 속도 향상
# input().strip() : 문자열 양쪽 공백(특히 개행) 제거

# 1) 첫 줄에서 N, M을 입력받음
#    - N: 듣도 못한 사람 수
#    - M: 보도 못한 사람 수

# 2) N개의 줄을 읽어서 set에 저장 (중복 제거 + 검색 빠름)
#    - heard = {이름1, 이름2, ...}

# 3) M개의 줄을 읽어서 set에 저장
#    - seen = {이름a, 이름b, ...}

# 4) 두 집합의 교집합을 구함
#    - both = heard & seen
#    - 집합 연산이므로 중복 자동 제거

# 5) 교집합 결과를 사전순으로 정렬
#    - sorted(both)

# 6) 출력
#    - 첫 줄: 교집합 원소 개수 (len(both))
#    - 다음 줄들: 정렬된 이름들 "\n".join(...)

