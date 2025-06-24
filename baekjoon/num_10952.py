# 250621

# 오른쪽 마우스 클릭 → Run Python File in Terminal

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True: 
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)



# ================================================
# while True:	입력을 계속 받기 위한 무한 루프
# map(int, input().split())	한 줄에 두 수 입력받음
# if a == 0 and b == 0:	종료 조건
# print(a + b)	정답 출력