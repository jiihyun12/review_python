# 250911

import math
import sys

input = sys.stdin.readline

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    # 2는 소수
    if x == 2:
        return True
    # 짝수이면 소수 아님
    if x % 2 == 0:
        return False
    # 홀수만 검사: 3,5,7,...,sqrt(x)
    limit = int(math.isqrt(x))
    for d in range(3, limit + 1, 2):
        if x % d == 0:
            return False
    return True

_ = int(input().strip())
nums = list(map(int, input().split()))

cnt = sum(1 for v in nums if is_prime(v))
print(cnt)

