# 250908

# 람다 : 이름 없이 한 줄로 만드는 작은 함수
# lambda 매개변수들: 표현식

# ============================================
# 1. 정수 n을 받아 n**2 + 2*n + 1 값을 반환하는 람다 함수를 작성하라

# poly = lambda n : (n + 1) ** 2

# n = int(input())
# print(poly(n))

# ============================================
# 2. 정수 n을 받아 짝수면 True, 홀수면 False를 반환하는 람다를 is_even에 담기

n2 = int(input())

# True if n2 % 2 == 0 else False
is_even = lambda n2 : n2 % 2 == 0
print(is_even(n2))

# 원라이너 방식
print((lambda n: n % 2 == 0)(int(input())))



