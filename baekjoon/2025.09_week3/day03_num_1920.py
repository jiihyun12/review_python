# 250916

# 주어진 수열 A 안에 어떤 수 x가 존재하는지 빠르게 판별

import sys
input = sys.stdin.readline

n = int(input().strip())
a = set(map(int, input().split()))
m = int(input().strip())
targets = list(map(int, input().split()))

for i in targets:
    if i in a:
        print(1)
    else:
        print(0)

 #=======================
 import sys
input = sys.stdin.readline

# N과 수열 A 입력
N = int(input().strip())
A = set(map(int, input().split()))  # set으로 만들어 중복 제거 + 탐색 빠르게

# M과 수열 M 입력
M = int(input().strip())
targets = list(map(int, input().split()))

# 각 원소가 A에 있으면 1, 없으면 0 출력
for x in targets:
    if x in A:       # 집합은 평균 O(1) 탐색
        print(1)
    else:
        print(0)
