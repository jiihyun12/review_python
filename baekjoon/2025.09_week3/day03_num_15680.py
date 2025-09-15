# 250915

N = int(input().strip())
print("YONSEI" if N == 0 else "Leading the Way to the Future")


# =================================

# 정수 N이 주어짐 (0 또는 1).
# N == 0이면 "YONSEI"
# N == 1이면 "Leading the Way to the Future" 출력

# 하나의 정수 N 입력 (0 또는 1)
N = int(input().strip())

# 조건에 따라 서로 다른 문자열 출력
if N == 0:
    print("YONSEI")
else:  # N == 1
    print("Leading the Way to the Future")
