# 251013

# 난쟁이는 9명이고, 각각의 키가 주어짐
# 그중 7명만 진짜 난쟁이이고, 그들의 키 합은 100

# 9명 중 2명만 가짜이고
# 그 두 명을 찾아서 제외한 뒤
# 남은 7명의 키를 오름차순으로 출력

heights = [int(input().strip()) for _ in range(9)]

total = sum(heights)
need = total - 100

seen = set()
fake_a = None
fake_b = None

for h in heights:
    complement = need - h
    if complement in seen:
        fake_a = h
        fake_b = complement
        break
    seen.add(h)

answer = heights[:]
answer.remove(fake_a)
answer.remove(fake_b)

for x in sorted(answer):
    print(x)


# =======================================

# 9명의 난쟁이 키를 입력받아 리스트에 저장
# 입력 예시: 20, 7, 23, 19, 10, 15, 25, 8, 13
heights = [int(input().strip()) for _ in range(9)]

# 9명의 키의 총합
total = sum(heights)

# 전체 합에서 100을 빼면, 그 차이는 '가짜 난쟁이 두 명의 합'
# 즉, 두 사람의 키 합이 need 값이 되어야 함.
need = total - 100


# seen: 이미 확인한 키 값을 저장할 집합 (중복 없이 빠른 탐색)
# fake_a, fake_b: 가짜 난쟁이 두 명을 저장할 변수
seen = set()
fake_a = None
fake_b = None


for h in heights:                 # 모든 난쟁이 키를 순회
    complement = need - h         # 현재 키와 더했을 때 need가 되는 값이 'complement'
    if complement in seen:        # 이미 본 키 중 complement가 있으면,
        fake_a = h                # 지금의 h가 가짜 중 한 명,
        fake_b = complement       # complement가 나머지 한 명
        break                     # 찾았으니 반복 종료
    seen.add(h)                   # 아직 못 찾았으면 현재 키를 seen에 추가

# 원본 리스트를 복사해서(answer),
# 찾은 두 명의 가짜 난쟁이 키를 제거
answer = heights[:]
answer.remove(fake_a)
answer.remove(fake_b)


# 남은 7명의 키를 오름차순 정렬해서 한 줄씩 출력
for x in sorted(answer):
    print(x)
