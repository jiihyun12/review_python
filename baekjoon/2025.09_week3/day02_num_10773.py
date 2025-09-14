# 250914

# 숫자가 들어오면 스택에 넣고, 0이 들어오면 직전 숫자 하나를 
# 마지막엔 스택에 남은 수들의 합을 출력

k = int(input())
stack = []

for _ in range(k):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))

#===============

# 입력: 첫 줄에 정수 K (명령 개수)
K = int(input())

stack = []  # 숫자를 담아둘 스택(리스트)

for _ in range(K):
    x = int(input())
    if x == 0:
        # 0이 나오면 직전에 적은 수를 지움
        # 문제 조건상 항상 지울 수 있는 0만 들어온다고 가정 가능
        stack.pop()
    else:
        # 0이 아니면 스택에 숫자 추가
        stack.append(x)

# 스택에 남은 모든 수의 합 출력
print(sum(stack))
