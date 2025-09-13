# 250914

# 명령을 받아 스택을 구현해서 결과를 출력


# 명령의 개수 입력
n = int(input())

# 파이썬 리스트를 스택처럼 사용
stack = []

# 명령의 개수만큼 반복
for _ in range(n):
    # 명령어를 입력받아 공백 기준으로 나눔
    # push X → ["push", "X"]
    # pop → ["pop"]
    cmd = input().split()

    # push 명령 처리
    if cmd[0] == 'push':
        # 두 번째 값(cmd[1])을 정수로 바꿔 스택에 넣음
        stack.append(int(cmd[1]))

    # pop 명령 처리
    elif cmd[0] == 'pop':
        if stack:              # 스택이 비어있지 않으면
            print(stack.pop()) # 맨 위 원소 꺼내서 출력
        else:                  # 스택이 비어있으면
            print(-1)          # -1 출력

    # size 명령 처리
    elif cmd[0] == 'size':
        # 스택에 들어있는 원소 개수 출력
        print(len(stack))

    # empty 명령 처리
    elif cmd[0] == 'empty':
        if stack:     # 스택이 비어있지 않으면
            print(0)  # 0 출력
        else:         # 스택이 비어있으면
            print(1)  # 1 출력

    # top 명령 처리
    elif cmd[0] == 'top':
        if stack:           # 스택이 비어있지 않으면
            print(stack[-1])# 맨 위 원소 출력 (삭제하지 않음)
        else:               # 스택이 비어있으면
            print(-1)       # -1 출력


# ===================
# 빠른 출력
import sys

input = sys.stdin.readline

n = int(input())
stack = []
out = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        out.append(str(stack.pop()) if stack else '-1')
    elif cmd[0] == 'size':
        out.append(str(len(stack)))
    elif cmd[0] == 'empty':
        out.append('0' if stack else '1')
    elif cmd[0] == 'top':
        out.append(str(stack[-1]) if stack else '-1')

print('\n'.join(out))

#
# input().split()으로 명령/인자를 한 번에 파싱.
# 출력은 out 리스트에 모았다가 마지막에 '\n'.join(...)으로 한 번에 출력 → 시간 절약.
# stack[-1]은 비어있지 않을 때만 접근! (비었으면 -1 처리)

    