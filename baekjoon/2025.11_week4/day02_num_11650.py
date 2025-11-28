# 251127

N = int(input().strip())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

def data(p):
    return (p[0], p[1])
points.sort(key=data)

for x, y in points:
    print(x, y)

# ==============================

# 첫 번째 줄: 점(point)의 개수 N 입력받음
# strip()은 혹시 모를 공백 제거
N = int(input().strip())

# 좌표를 저장할 빈 리스트 준비
points = []

# N번 반복하면서 좌표를 입력받는다
for _ in range(N):
    # 각 줄에서 x, y 두 정수를 입력받아 튜플 형태로 저장할 준비
    x, y = map(int, input().split())
    # 하나의 좌표를 (x, y) 튜플로 리스트에 추가
    points.append((x, y))


# 정렬 기준 함수 정의
# p는 (x, y) 한 점을 의미한다.
# 이 함수는 "정렬 기준값"으로 (x, y) 튜플 자체를 반환한다.
# 파이썬은 튜플을 정렬할 때 앞에서부터 비교하므로
# 1) x 기준 오름차순
# 2) x가 같으면 y 기준 오름차순
# 으로 자동 정렬된다.
def data(p):
    return (p[0], p[1])   # p는 (x, y) → p[0] = x, p[1] = y


# sort()에 key 함수를 넣어서 정렬 기준을 정한다
# key=data 라는 말은 “정렬할 때 data(p)로 나온 값을 기준으로 정렬해라”
points.sort(key=data)


# 정렬된 좌표들을 차례대로 출력
for x, y in points:
    print(x, y)


# ================================
# def data(p): return (p[0], p[1])
# 정렬 기준 함수
# 정렬할 때 (x, y) 순으로 비교하라는 의미

# points.sort(key=data)
# 정렬 기준으로 위 함수를 사용
# x 오름차순 → x가 같으면 y 오름차순

# 반복 + 출력
# 입력된 좌표를 정렬해서 그대로 출력
