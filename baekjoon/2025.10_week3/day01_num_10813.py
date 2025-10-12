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

