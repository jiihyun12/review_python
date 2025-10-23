# 251022

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = ''
    for c in S:
        result += c * R
    print(result)

# ============================

# T = int(input())
# 테스트케이스 수 입력받기

# for _ in range(T):
# 테스트케이스 개수만큼 반복

# R, S = input().split()
# 한 줄에서 R(반복 횟수)와 S(문자열) 분리
# R은 문자열이므로 int(R)로 변환

# for c in S:
# 문자열의 각 문자를 꺼내서

# result += c * R
# 문자를 R번 반복한 뒤 결과 문자열에 더함

# print(result)
# 한 테스트케이스의 결과를 출력