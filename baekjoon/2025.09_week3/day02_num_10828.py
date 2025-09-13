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

    