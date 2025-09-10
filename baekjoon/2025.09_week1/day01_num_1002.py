# 2509010

import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if d == 0 and r1 == r2:
        print(-1)  # 무한대
    elif d == 0 and r1 != r2:
        print(0)   # 동심원, 반지름 다름
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)   # 외접 or 내접
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)   # 두 점에서 만남
    else:
        print(0)   # 그 외 (겹치지 않음)


