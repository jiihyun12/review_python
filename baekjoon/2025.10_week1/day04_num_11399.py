# 251003

import sys
input = sys.stdin.readline

N = int(input())

times = list(map(int, input().split()))

times.sort()

total = 0      
current = 0    

for t in times:
    current += t    
    total += current  

print(total)

# ============================

import sys
input = sys.stdin.readline

# 사람 수 입력
N = int(input())

# 각 사람이 돈 인출에 걸리는 시간
times = list(map(int, input().split()))

# 1) 오름차순 정렬 (작은 사람이 먼저)
times.sort()

# 2) 누적합을 계산
total = 0      # 총 대기 시간의 합
current = 0    # 지금까지의 누적합 (앞사람들 포함한 대기 시간)

for t in times:
    current += t    # 이번 사람의 인출 시간 누적
    total += current  # 누적합을 총합에 더함

print(total)
