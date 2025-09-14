# 250914

def add(a,b):
    return a + b

while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    print(add(a,b))

# 여러 줄에 걸쳐 A B가 주어짐 (A, B는 친구 수).
# A와 B가 둘 다 0이면 입력 종료.
# 각 줄마다 A + B를 출력.