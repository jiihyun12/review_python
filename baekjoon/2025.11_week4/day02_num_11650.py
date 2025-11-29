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

# 각 점을 (x, y) 튜플로 리스트에 저장
# sort()에 key를 줘서 (x, y) 기준으로 정렬

# 파이썬에서 튜플은 앞에서부터 차례대로 비교하니까
# (x, y)로 정렬하면 자동으로
# x 먼저 비교 --> 같으면 y 비교
