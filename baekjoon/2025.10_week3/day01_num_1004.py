# 251013

import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

def inside(px, py, cx, cy, r):
    return (px - cx) * (px - cx) + (py - cy) * (py - cy) < r * r

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    
    n = int(input())
    default = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        s_in = inside(x1, y1, cx, cy, r)
        e_in = inside(x2, y2, cx, cy, r)
        if s_in ^ e_in:
            default += 1
    print(default)

# =================================

import sys
input = sys.stdin.readline  # 빠른 입력

def inside(px, py, cx, cy, r):
    # 점(px, py)가 원(cx, cy, r) 내부에 있는지 판별
    # 거리^2 = (px - cx)^2 + (py - cy)^2
    return (px - cx) * (px - cx) + (py - cy) * (py - cy) < r * r

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    # 출발점(x1, y1), 도착점(x2, y2)
    x1, y1, x2, y2 = map(int, input().split())
    
    n = int(input())  # 원(행성계)의 개수
    default = 0       # 통과 횟수 누적

    for _ in range(n):
        cx, cy, r = map(int, input().split())  # 각 원의 중심과 반지름
        
        # 출발점과 도착점 각각이 이 원 내부에 있는지 확인
        s_in = inside(x1, y1, cx, cy, r)
        e_in = inside(x2, y2, cx, cy, r)
        
        # 한쪽만 내부(True/False가 다를 때만 경계를 지난 것)
        if s_in ^ e_in:
            default += 1
    
    # 해당 테스트 케이스 결과 출력
    print(default)

