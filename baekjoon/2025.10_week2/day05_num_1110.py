# 251011

current = int(input())
current = org

count = 0
while True:
    a = current // 10
    b = current % 10
    c = (a + b) % 10

    new_number = b * 10 + c
    count += 1

    if new_number == org:
        break
    else:
        current = new_number
        
print(count)




# =============================================
# 주어진 수가 다시 자기 자신으로 돌아올 때까지 그 수를 특정 규칙으로 계속 변환하면서
# 몇 번 변환했는지 사이클 길이를 구하는 문제


# 1. 처음 입력값을 받는다.
# 입력은 0~99 사이의 정수 하나.
org = int(input())

# 이 문제는 '처음 수로 다시 돌아올 때까지 몇 번 변했는가'를 구하는 거니까,
# 현재 숫자(current)도 처음엔 org와 같게 설정한다.
current = org

# 사이클(변환) 횟수를 세기 위한 변수
count = 0

# 2. 무한 반복 (언제 멈출지 모르니까 while True)
while True:
    # (1) 현재 숫자의 십의 자리와 일의 자리를 분리
    a = current // 10   # 십의 자리
    b = current % 10    # 일의 자리

    # (2) 두 자리의 합의 "일의 자리"를 구한다.
    # 예: 2+6=8 → 8, 8+4=12 → 2
    c = (a + b) % 10

    # (3) 새로 만들어질 수는
    #     현재 수의 일의 자리(b)와, 합의 일의 자리(c)를 붙여 만든다.
    # 예: current=26 → b=6, c=8 → new_number=68
    new_number = b * 10 + c

    # (4) 한 번 변환했으니까 카운트를 증가
    count += 1

    # (5) 새로 만들어진 수가 처음 입력값(org)과 같으면 멈춘다.
    if new_number == org:
        break
    else:
        # 아직 같지 않으면, 새 수를 current로 바꿔서 다음 사이클로 이동
        current = new_number

# 3. while문이 끝났다는 건, 처음 숫자로 되돌아왔다는 뜻
#     지금까지 몇 번 돌았는지를 출력
print(count)
