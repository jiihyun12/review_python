# 251026

numbers1 = int(input())
numbers2  = list(map(int, input().split()))

minNums = min(numbers2)
maxNums = max(numbers2)

print(minNums, maxNums)

# ===========================

# 첫 번째 줄: 정수의 개수 N 입력 (사실 이후에 바로 안 써도 됨)
N = int(input())

# 두 번째 줄: N개의 정수를 입력받아서 리스트로 저장
# input().split()  → 입력 문자열을 공백 기준으로 나눔 (문자열 리스트)
# map(int, ...)   → 각 문자열을 int로 변환 (map 객체 생성)
# list(...)       → map 객체를 리스트로 변환
numbers = list(map(int, input().split()))

# 리스트에서 최솟값과 최댓값을 구함
min_value = min(numbers)
max_value = max(numbers)

# 공백으로 구분해서 출력
print(min_value, max_value)
