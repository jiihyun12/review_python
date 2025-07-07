# 250707

# 두 개의 행렬을 받아서 같은 위치끼리 더한 결과를 출력한다.

n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j] + b[i][j])
    print(*row)

# ========================================

# 첫 줄에서 행의 개수 n, 열의 개수 m을 입력받아 정수형으로 저장
n,m = map(int, input().aplit())

# 첫 번째 행렬 A를 저장할 리스트
a = []

# 두 번째 행렬 B를 저장할 리스트
b = []

# a 행렬을 입력받는 부분
# 총 n 줄에 걸쳐 m개의 숫자를 입력 받아 리스트에 저장한다.
for _ in range(n):
    # 한 줄에 공백으로 나뉜 m개의 숫자를 정수형으로 변환해 리스트로 만든 후 A에 추가한다.
    a.append(list(map(int, input().split())))

# b 행렬도 a와 마찬ㄷ가지로 n줄에 걸쳐 입력받는다.
for _ in range(n):
    b.append(list(map(int, input().split())))

# 두 행렬의 같은 위치에 있는 값들을 더해 출력하는 부분
for i in range(n):  # 각 행(row) 반복
    row = []        # 결과를 저장할 새로운 행 리스트
    for j in range(m):  # 각 열(column) 반복
        # A와 B의 같은 위치(i행 j열) 값을 더해서 row에 추가
        row.append(a[i][j] + b[i][j])
    # 완성된 한 행을 공백으로 나눠서 출력
    print(*row) # --> 리스트 안의 값을 묶음 풀기(unpack) 해서 출력