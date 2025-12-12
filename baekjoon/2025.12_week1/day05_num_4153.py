# 251212

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    sides = [a, b, c]
    sides.sort()       
    x, y, h = sides[0], sides[1], sides[2]
    if x*x + y*y == h*h:
        print("right")
    else:
        print("wrong")


# ===============================================

# 세 변이 주어졌을 때 직각삼각형인지 판별하는 문제

# 직각삼각형의 조건은
# 가장 긴 변² = (나머지 두 변² 합)
# 예를 들어 3, 4, 5라면:
# 가장 긴 변 = 5
# 검사:
# 5² = 25
# 3² + 4² = 9 + 16 = 25
# 같으니까 직각삼각형 --> "right"


# 입력이 계속 주어지다가
# 0 0 0이 나오면 종료
# 각 줄에는 세 변의 길이 a, b, c가 들어있음
# 세 변으로 직각삼각형이면 --> right, 아니면 --> wrong

# 설계
# -->
#입력을 반복해서 받는다.
# 0 0 0이면 종료한다.
# 세 변 중 가장 큰 숫자를 찾는다.
# 나머지 두 변과 비교해서 피타고라스 관계 확인한다.
# 맞으면 "right", 아니면 "wrong" 출력.


while True:
    a, b, c = map(int, input().split())

    # 0 0 0 입력되면 반복 종료
    if a == 0 and b == 0 and c == 0:
        break

    # 3개의 길이를 리스트로 묶고
    sides = [a, b, c]

    # 가장 긴 변을 찾기 위해 정렬 (오름차순)
    sides.sort()        # 예: [3, 4, 5]

    # 변수 의미:
    # x, y: 짧은 두 변
    # h: 가장 긴 변
    x, y, h = sides[0], sides[1], sides[2]

    # 피타고라스 정리 검사
    if x*x + y*y == h*h:
        print("right")
    else:
        print("wrong")
