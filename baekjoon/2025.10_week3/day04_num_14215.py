# 251018

a, b, c = sorted(map(int, input().split()))  

if a + b > c:
    print(a + b + c)            
else:
    print(2 * (a + b) - 1)       

# =====================================

# 세 막대의 길이가 주어졌을 때, 삼각형이 될 수 있는 가장 큰 둘레를 구하는 문제

# a ≤ b ≤ c   (c는 가장 긴 막대)
# 삼각형 조건 : a + b > c
# 만약 이게 참이면 삼각형 가능 --> 둘레 = a + b + c
# 만약 거짓이면 삼각형 불가능 --> 가장 긴 막대를 줄여야 함 
# a + b + (a + b - 1) = 2*(a + b) - 1

a, b, c = sorted(map(int, input().split()))  # 세 막대 길이 정렬 (a≤b≤c)

# 삼각형 조건 확인
if a + b > c:
    print(a + b + c)             # 삼각형 가능 → 그냥 둘레 출력
else:
    print(2 * (a + b) - 1)       # 삼각형 불가능 → 가장 긴 변 줄임
