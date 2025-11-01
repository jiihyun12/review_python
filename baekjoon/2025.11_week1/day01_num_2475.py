# 251101

nums = list(map(int, input().split()))
result = 0

for i in nums:
    result += i ** 2
print(result % 10)

# ========================

입력: 한 줄에 공백으로 구분된 5개의 숫자 (0~9)
출력: 각 숫자의 제곱을 모두 더한 후 10으로 나눈 나머지

숫자 5개를 한 줄로 입력받기 --> split() 사용
각 숫자를 int로 변환해서 제곱한 값을 모두 더함
합계를 10으로 나눈 나머지를 출력

nums = list(map(int, input().split()))  # 5개 숫자 입력받기
total = 0
for n in nums:
    total += n ** 2                     # 제곱 후 누적합
print(total % 10)                       # 10으로 나눈 나머지 출력
