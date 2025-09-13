# 250914

n = int(input())

result = 0

for m in range(1, n + 1):       # 1부터 n까지 반복
    value = sum(map(int, str(m)))  # m의 각 자리수 합
    if m + value == n:             # 분해합이 n과 같으면
        result = m                 # 생성자 찾음
        break                      # 가장 작은 생성자만 필요하니 바로 종료

print(result)
