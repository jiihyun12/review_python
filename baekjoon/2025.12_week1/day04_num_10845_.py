# 251210

import sys
from collections import deque

input = sys.stdin.readline   
N = int(input())             

q = deque()                 

for _ in range(N):
    cmd = input().split()  

    if cmd[0] == "push":
        q.append(cmd[1])

    elif cmd[0] == "pop":
        if q:
            print(q.popleft()) 
        else:
            print(-1)

    elif cmd[0] == "size":
        print(len(q))         

    elif cmd[0] == "empty":
        print(0 if q else 1)

    elif cmd[0] == "front":
        if q:
            print(q[0])       
        else:
            print(-1)

    elif cmd[0] == "back":
        if q:
            print(q[-1])    
        else:
            print(-1)


# =========================

# push X	큐의 뒤에 X를 넣는다
# pop	큐의 앞에서 하나 빼고 출력, 없으면 -1
# size	큐 길이 출력
# empty	비어있으면 1, 아니면 0
# front	가장 앞 값 출력, 없으면 -1
# back	가장 뒤 값 출력, 없으면 -1

# 데이터를 저장할 컨테이너(자료구조) 하나 필요
# 여기에 대해 위 6개 함수(동작)를 구현해야 함   
# class MyQueue:
#     def push(x): ...
#     def pop(): ...
#     def size(): ...
#     def empty(): ...
#     def front(): ...
#     def back(): ...



# ==========================

# 큐는 앞에서 빼고 뒤에 넣는 자료구조라
# 리스트로 구현하면 pop(0)이 느리다
# deque는 이걸 O(1)로 해줌 
# 그래서 deque 사용

# 명령어 문자열을 split()해서
# 첫 번째 토큰: 명령 이름 (cmd[0])s
# 두 번째 토큰: 인자 (cmd[1], push일 때만 존재)
# 각 명령을 설계한 큐의 6개 동작에 매핑해서 처리

import sys
from collections import deque

input = sys.stdin.readline   # 입력이 많으므로, 기본 input()보다 빠른 버전 사용

N = int(input())             # 명령의 개수

q = deque()                  # 우리가 사용할 큐(실제로는 덱이지만, 큐처럼 쓸 거임)

for _ in range(N):
    cmd = input().split()    # 명령 한 줄 입력 → 공백 기준 분리
                             # 예: "push 3" → ["push", "3"]
                             #     "pop"    → ["pop"]

    if cmd[0] == "push":
        # cmd[1]에는 push 뒤에 오는 숫자가 들어 있다.
        # 큐의 "뒤"에 원소를 넣는 동작
        q.append(cmd[1])

    elif cmd[0] == "pop":
        # pop은 "맨 앞"에서 꺼내야 한다.
        if q:               # 큐가 비어 있지 않으면
            # popleft()는 가장 왼쪽 요소를 꺼내면서 반환
            print(q.popleft())
        else:
            # 큐가 비어 있으면 -1 출력
            print(-1)

    elif cmd[0] == "size":
        # 현재 큐에 들어있는 원소 개수
        print(len(q))

    elif cmd[0] == "empty":
        # 비어있으면 1, 아니면 0
        # deque는 비어있으면 False, 있으면 True 로 평가되기 때문에
        # not q → 비어있으면 True
        print(1 if not q else 0)

    elif cmd[0] == "front":
        # 맨 앞의 값 보는 거 (꺼내지는 않음)
        if q:
            print(q[0])     # 가장 왼쪽(앞)의 요소
        else:
            print(-1)

    elif cmd[0] == "back":
        # 맨 뒤의 값 보는 거 (꺼내지는 않음)
        if q:
            print(q[-1])    # 가장 오른쪽(뒤)의 요소
        else:
            print(-1)
