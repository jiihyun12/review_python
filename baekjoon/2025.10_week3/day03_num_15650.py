import sys
input = sys.stdin.readline

N, M = map(int, input().split())

seq = []

def result(start, depth):
    if depth == M:
        print(*seq)    
        return
    for x in range(start, N + 1):
        seq.append(x)
        result(x + 1, depth + 1)
        seq.pop()

result(1, 0)
