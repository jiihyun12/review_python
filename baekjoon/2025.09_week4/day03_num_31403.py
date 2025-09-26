# 250926

# (A + B) - C (정수 계산)
A, B, C = map(int, input().split())
result1 = (int(A) + int(B)) - int(C)
print(result1)

# (A와 B를 문자열로 이어붙인 뒤, 정수로 바꾼 값) - C
result2 = int(str(A) + str(B)) - int(C)
print(result2)


# =========================

# 입력: 한 줄에 A, B, C
A, B, C = map(int, input().split())

# 1. (A + B) - C : 정수 계산
result1 = (A + B) - C
print(result1)

# 2. (A와 B를 문자열로 이어붙인 뒤 정수로 변환) - C
#    예: A=10, B=20 → "1020" → int("1020")=1020
result2 = int(str(A) + str(B)) - C
print(result2)


# ===================================

# 정답
# A, B, C가 한 줄씩!
A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

print((A + B) - C)
print(int(str(A) + str(B)) - C)