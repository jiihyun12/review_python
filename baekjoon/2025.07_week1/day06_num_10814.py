# 250705

N = int(input())

nameandage = []

for i in range(N):
    age, name = input().split()
    nameandage.append((int(age), name))
nameandage.sort(key=lambda x: x[0])

for age, name in nameandage:
    print(age, name)

#========================================
# N = int(input())  # 몇 명인지 입력받기
# nameandage = []   # (나이, 이름) 저장할 리스트

# # N번 반복해서 나이와 이름을 입력받고 리스트에 추가
# for _ in range(N):
#     age, name = input().split()
#     nameandage.append((int(age), name))

# # 나이 기준으로 정렬 (같은 나이면 입력 순서 유지됨)
# nameandage.sort(key=lambda x: x[0])
# 리스트를 정렬하되, 각 항목의 x[0] 값을 기준으로 정렬해라"라는 뜻
# x[0]은 각 튜플의 첫 번째 값 → 즉 age
# nameandage.sort(key=lambda x: x[0])

# # 정렬된 결과 출력
# for age, name in nameandage:
#     print(age, name)
