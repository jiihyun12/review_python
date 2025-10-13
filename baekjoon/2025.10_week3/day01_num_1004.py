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
