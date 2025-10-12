# 251013

N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(i + 1)

for _ in range(M):
    i, j = map(int, input().split())

    temp = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = temp

for x in basket:
    print(x, end=' ')

# ========================================

# 바구니가 1번부터 N번까지 있고
# 처음엔 [1, 2, 3, 4, ..., N] 들어 있음
# 두 바구니의 공을 몇 번 바꾼 뒤
# 마지막 상태를 출력

# 1. 바구니 개수 N, 바꾸는 횟수 M 입력
N, M = map(int, input().split())

# 2. 바구니를 만든다 (1번 바구니엔 1, 2번엔 2 ... )
basket = []
for i in range(N):
    basket.append(i + 1)
# ex) N=5 --> basket = [1, 2, 3, 4, 5]

# 3. 공을 바꾸는 과정
for _ in range(M):
    # i, j는 바꿀 바구니 번호
    i, j = map(int, input().split())

    # (1) i번째 공을 임시로 저장
    temp = basket[i - 1]

    # (2) j번째 공을 i번째 자리에 넣기
    basket[i - 1] = basket[j - 1]

    # (3) temp(원래 i번째 공)를 j번째 자리에 넣기
    basket[j - 1] = temp

# 4. 결과 출력 (공백으로 나열)
for x in basket:
    print(x, end=' ')
