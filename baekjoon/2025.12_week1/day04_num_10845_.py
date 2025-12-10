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


import sys
from collections import deque

input = sys.stdin.readline   # 빠른 입력
N = int(input())             # 명령 개수 입력

q = deque()                  # 큐 초기화

for _ in range(N):
    cmd = input().split()    # 명령어를 공백 기준으로 분리

    # push X 형태인지 확인
    if cmd[0] == "push":
        # 큐의 뒤에 cmd[1]을 넣는다
        q.append(cmd[1])

    elif cmd[0] == "pop":
        # 큐가 비어 있으면 -1 출력
        if q:
            print(q.popleft())  # 앞에서 하나 꺼내 출력
        else:
            print(-1)

    elif cmd[0] == "size":
        print(len(q))          # 큐의 길이 출력

    elif cmd[0] == "empty":
        # 비어 있으면 1, 아니면 0
        print(0 if q else 1)

    elif cmd[0] == "front":
        if q:
            print(q[0])        # 가장 앞 요소
        else:
            print(-1)

    elif cmd[0] == "back":
        if q:
            print(q[-1])       # 가장 뒤 요소
        else:
            print(-1)
