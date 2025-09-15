# 250915

# 점(x,y)들을 y좌표 오름차순, y 같으면 x 오름차순으로 정렬해 출력

import sys
input = sys.stdin.readline  # 많은 줄을 빨리 읽기 위함 

n = int(input().strip())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))   # (x, y) 튜플로 저장

# 정렬 기준:
# 1) y 오름차순
# 2) y가 같으면 x 오름차순
points.sort(key=lambda p: (p[1], p[0]))

# 출력: 각 줄에 "x y"
out = []
for x, y in points:
    out.append(f"{x} {y}")
print("\n".join(out))



