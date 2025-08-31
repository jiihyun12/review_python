# 250831

# 2309 - 일곱 난쟁이 (조합 사용 버전)
# 아이디어:
#  - 9명 중 7명을 고르는 모든 조합(총 36개)을 검사하여
#    합이 정확히 100인 조합을 찾는다.
#  - 찾으면 정렬하여 출력하고 종료.

from itertools import combinations

# 9명의 키 입력
heights = [int(input().strip()) for _ in range(9)]

# 7명 조합을 모두 시도
for comb in combinations(heights, 7):
    # 합이 100이면 정답
    if sum(comb) == 100:
        for h in sorted(comb):  # 오름차순 출력
            print(h)
        break  # 찾았으니 종료


# 9명의 키 합을 S라고 하면, 가짜 2명의 합은 S - 100
# 9명 중 두 명 (i, j)를 찾아서 heights[i] + heights[j] == S - 100이면 그 둘을 빼고 남은 7명을 오름차순으로 출력

# ------------------------

# itertools 모듈에서 combinations 가져온다.

# combinations
# 형식: combinations(iterable, r)
# 의미: iterable에서 순서와 상관없이, 중복 없이 r개를 뽑는 모든 경우를 차례로 내놓는 이터레이터를 돌려줌
# 반환 형태: 각 경우는 튜플로 나옴

# --------------------------
# 다른 방법

# - 9명 키의 합을 total이라고 하면, '가짜 2명의 합'은 need = total - 100
# - 즉, 9명 중에서 두 수의 합이 need가 되는 '그 두 명'만 찾아서 빼면,
#   나머지 7명이 진짜 난쟁이!

# 1) 입력 받기: 난쟁이 9명의 키를 차례로 읽어서 리스트에 담는다.
heights = []
for _ in range(9):
    # input()으로 한 줄 읽고, 줄끝 개행 제거(strip), 정수로 변환(int)
    num = int(input().strip())
    heights.append(num)

# 2) 전체 합과 '빼야 하는 합(=가짜 둘의 합)'을 계산
total = sum(heights)   # 9명의 키 합
need = total - 100     # 가짜 2명의 합 (이 합을 만드는 두 명을 찾으면 됨)

# 3) 지금까지 본 키들을 저장할 '집합(set)'
#    - set은 같은 값을 여러 번 넣어도 한 번만 저장되는 자료구조
#    - "값이 들어있나?"를 빠르게 검사할 수 있어 초보자에게도 직관적
seen = set()

# 4) 찾은 가짜 두 명의 키를 저장할 변수 (처음엔 모름)
fake_a = None
fake_b = None

# 5) 한 번만 도는 반복문으로 가짜 두 명 찾기
#    어떤 키 h를 보고 있을 때,
#    'need - h' 라는 값이 이전에 본 적이 있다면,
#    (need - h) + h == need 이므로 이 둘이 바로 가짜 두 명!
for h in heights:
    complement = need - h     # h와 더하면 need가 되는 '짝'(보수, complement)

    # 이전에 본 키들(seen) 안에 complement가 있으면 가짜 둘을 찾은 것!
    if complement in seen:
        fake_a = h
        fake_b = complement
        break  # 더 볼 필요 없이 바로 종료

    # 아직 못 찾았다면, 현재 키 h를 "본 적 있음"으로 표시
    seen.add(h)

# 6) 이제 찾은 두 명(fake_a, fake_b)을 리스트에서 제거한다.
#    - list.remove(x): 리스트에서 '처음 발견되는 x' 하나를 삭제
#    - 같은 키가 두 번 나올 수 있으니 remove를 두 번 호출한다.
answer = heights[:]  # 원본 보존을 위해 복사본 사용
answer.remove(fake_a)
answer.remove(fake_b)

# 7) 남은 7명(진짜 난쟁이) 키를 오름차순으로 정렬 후 출력
answer.sort()
for x in answer:
    print(x)

#-------
# 9명의 합에서 100을 뺀 값 need 를 먼저 만든 다음, 한 번만 훑으면서
# 현재 숫자 h + 이전에 본 어떤 숫자 = need?만 체크
# seen은 그냥 지금까지 본 숫자 보관함
# if complement in seen: 한 줄이 짝이 있었는지를 알려준다.
# 같은 수가 두 번 필요한 경우(예: 45와 45)도, 두 번째 45를 볼 때
# 첫 번째 45가 이미 seen에 있으므로 정상적으로 잡힘