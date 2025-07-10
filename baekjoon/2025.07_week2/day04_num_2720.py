# 250710

# 거스름돈을 동전으로 최소 개수로 바꿔주는 문제

# 손님에게 줄 거스름돈이 주어졌을 때
# 쿼터(25센트), 다임(10센트), 니켈(5센트), 페니(1센트)
# 이 4종류의 동전을 이용해
# 가장 적은 개수의 동전으로 거슬러 주세요.

T = int(input()) 

for i in range(T):
    money = int(input())  

    if money >= 25:
        quarter = money // 25
        money = money % 25
    else:
        quarter = 0

    if money >= 10:
        dime = money // 10
        money = money % 10
    else:
        dime = 0

    if money >= 5:
        nickel = money // 5
        money = money % 5
    else:
        nickel = 0

    penny = money

    print(quarter, dime, nickel, penny)

# ==============================================
# 1.
# 큰 동전부터 차례대로 나눠서 개수를 구하고
# 남은 돈으로 다음 동전 계산하기
    
# "돈을 가장 큰 동전부터 나눠서 최대한 쓰고, 남는 건 다음으로 처리한다"
# 예: 124센트
# 25로 나누면 4개 → 100센트 사용 → 24 남음
# 10으로 나누면 2개 → 20센트 사용 → 4 남음
# 5는 못 씀 (0개)
# 1로 4개

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    change = int(input())  # 거스름돈 (센트 단위)

    q = change // 25       # 쿼터 개수
    change %= 25           # 남은 돈

    d = change // 10       # 다임 개수
    change %= 10

    n = change // 5        # 니켈 개수
    change %= 5

    p = change             # 나머지는 전부 페니

    print(q, d, n, p)


# -------
# 2.

# 돈이 25 이상이면 → 몇 개 있는지 계산하고 남기기
# 남은 돈이 10 이상이면 → 다임 계산
# 남은 돈이 5 이상이면 → 니켈 계산
# 나머지는 무조건 페니

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    money = int(input())  # 거스름돈 입력

    if money >= 25:
        q = money // 25
        money = money % 25
    else:
        q = 0

    if money >= 10:
        d = money // 10
        money = money % 10
    else:
        d = 0

    if money >= 5:
        n = money // 5
        money = money % 5
    else:
        n = 0

    # 남은 돈은 무조건 페니로
    p = money

    print(q, d, n, p)

