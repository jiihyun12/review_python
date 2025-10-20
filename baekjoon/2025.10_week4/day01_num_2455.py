# 251020

import sys
input = sys.stdin.readline

train = 0
maxI = 0

for _ in range(4):
    a, b = map(int, input().split())
    train = train - a + b
    
    if train > maxI:
        maxI = train

print(maxI)

# =======================

import sys
input = sys.stdin.readline

train = 0     # 현재 기차 안 인원
maxI = 0      # 지금까지의 최대 인원

for _ in range(4):
    a, b = map(int, input().split())  # a: 내린 사람, b: 탄 사람
    train = train - a + b             # 현재 인원 갱신
    if train > maxI:                  # 최대 인원 갱신
        maxI = train

print(maxI)  # 마지막에 최대값 출력!
