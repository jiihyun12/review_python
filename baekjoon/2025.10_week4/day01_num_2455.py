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