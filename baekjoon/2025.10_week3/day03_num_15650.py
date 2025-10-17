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


# ======================================

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

seq = []

def result(start, depth):
    # depth가 M이면 지금까지 뽑은 seq를 문제 형식(공백으로)로 출력
    if depth == M:
        print(*seq)     # <-- 여기서 *를 써서 리스트를 풀어 공백으로 출력해야 함
        return
    # start부터 N까지 숫자를 하나씩 선택 (오름차순 유지)
    for x in range(start, N + 1):
        seq.append(x)
        result(x + 1, depth + 1)
        seq.pop()

result(1, 0)

# * --> 리스트를 풀어서(unpack) 출력하거나 함수 인자로 전달할 때 쓰는 문법
# ex) 
# nums = [1, 2, 3]
# print(nums) --> [1,2,3]
# print(*nums) --> 1,2,3

# ex)
# def add(a, b, c):
#     return a + b + c
# nums = [1, 2, 3]
# print(add(*nums))  # 언패킹해서 add(1, 2, 3) 과 동일