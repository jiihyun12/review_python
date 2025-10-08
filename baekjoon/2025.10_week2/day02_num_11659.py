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



