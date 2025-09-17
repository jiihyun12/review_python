# N: 동전 종류 수, K: 목표 금액
N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input().strip()))

coins.sort(reverse=True)  # 큰 동전부터 사용하기 위해 내림차순 정렬

count = 0  # 사용한 동전 개수

for coin in coins:
    if K == 0:
        break  # 남은 금액이 없으면 종료

    if coin <= K:
        # 이 동전을 몇 개 쓸 수 있는지 계산
        use = K // coin
        count += use
        K %= coin  # 남은 금액 갱신

print(count)
