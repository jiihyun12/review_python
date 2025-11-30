# 251129

from collections import deque

N = int(input())
q = deque(range(1, N + 1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])


##
from collections import deque   # deque 자료구조를 쓰기 위해 불러온다 (큐 역할)

N = int(input())                # 카드 개수 N 입력 (1부터 N까지 카드가 있다고 가정)

# 1부터 N까지 숫자를 차례대로 담은 deque 생성
# range(1, N+1)은 1,2,3,...,N 까지 숫자를 만들어줌
q = deque(range(1, N + 1))

# 카드가 1장 남을 때까지 계속 반복
while len(q) > 1:
    q.popleft()                 # 1) 맨 위 카드 버리기 (큐의 앞에서 하나 꺼내서 버림)

    # 2) 그 다음 카드도 앞에서 꺼내서 (popleft)
    #    그 카드를 다시 맨 뒤에 붙인다(append) → "위에서 빼서 아래로 보내기"
    q.append(q.popleft())

# 반복이 끝나면 카드가 1장만 남아 있음
# 그 남은 카드(맨 앞 카드)를 출력
print(q[0])


# 예를 들어 N = 6이면,
# 초기 상태: q = [1, 2, 3, 4, 5, 6]

# 1버림 --> [2, 3, 4, 5, 6]
# 2를 뒤로 → [3, 4, 5, 6, 2]

# 3버림 --> [4, 5, 6, 2]
# 4를 뒤로 → [5, 6, 2, 4]

# 5버림 --> [6, 2, 4]
# 6을 뒤로 → [2, 4, 6]

# 2버림 --> [4, 6]
# 4를 뒤로 --> [6, 4]

# 6버림 --> [4]

# 그래서 마지막 카드 = 4 --> print(q[0]) 에서 4 출력

# ====================================================

# deque 없는 방법
N = int(input())

p = 1
while p * 2 <= N:
    p *= 2

if N == p:
    print(N)
else:
    print((N - p) * 2)


##

