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


