# 250628

# N: 숫자의 개수, X: 기준값
N, X = map(int, input().split())

# N개의 숫자를 리스트로 입력받기
A = list(map(int, input().split()))

# 조건에 맞는 숫자들만 출력
for num in A:
    if num < X:
        print(num, end=' ')

# ==================================
# map(int, input().split())	공백 구분 정수 입력
# for num in A:	리스트 순회
# if num < X:	조건 비교
# print(num, end=' ')	줄바꿈 없이 공백 출력


# ========================================
# 문자열로 붙이기

n, x = map(int, input().split())
a = list(map(int, input().split()))

result = (' '.join(str(i) for i in a if i < x))
print(result)

# 
# n, x = map(int, input().split())	첫 줄에서 숫자 개수 n, 기준값 x 받음
# a = list(map(int, input().split()))	두 번째 줄에서 숫자 리스트 받음
# ' '.join(...)	조건에 맞는 숫자를 문자열로 바꿔 공백으로 붙임
# print(result)	한 줄로 출력


# 또는 
n, x = map(int, input().split())
a = list(map(int, input().split()))

result = ''  # 출력할 문자열

for i in a:
    if i < x:
        result += str(i) + ' '  # 문자열로 바꿔서 공백 붙여서 누적

print(result.strip())  # 마지막 공백 제거


