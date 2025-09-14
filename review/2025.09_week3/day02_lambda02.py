# 250914

# 정수 n을 입력받아 절댓값을 반환하는 람다를 abs_like에 담아 출력
# 단, 파이썬의 abs()는 사용하지 말 것

n = int(input())

abs_lambda = lambda n : n if n >= 0 else -n 
print(abs_lambda(n))


# n >= 0 이면 그냥 n
# n < 0 이면 → -n