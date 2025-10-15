# 251015

import sys
input = sys.stdin.readline

n = int(input())

MOD = 10007

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp1, dp2 = 1, 2   
    for _ in range(3, n + 1):
        dp1, dp2 = dp2, (dp1 + dp2) % MOD
    print(dp2 % MOD)
