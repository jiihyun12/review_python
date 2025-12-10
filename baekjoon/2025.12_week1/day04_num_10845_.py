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
