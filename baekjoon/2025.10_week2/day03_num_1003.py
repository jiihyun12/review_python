# 251008

test = int(input())

count_zero = [0] * 41
count_one = [0] * 41

count_zero[0], count_one[0] = 1, 0
count_zero[1], count_one[1] = 0, 1

for i in range(2, 41):
    count_zero[i] = count_zero[i - 1] + count_zero[i - 2]
    count_one[i] = count_one[i - 1] + count_one[i - 2]

for _ in range(test):
    data = int(input())
    print(count_zero[data], count_one[data])



# ====================================

n이 주어졌을 때,
위의 함수 fibonacci(n)을 실행하면
숫자 0과 1이 각각 몇 번 출력 되는지?


# 테스트 케이스 개수 입력
# 예를 들어 3이면 -> 3번 반복해서 숫자를 입력받고 결과를 출력함
test = int(input())

# n이 최대 40까지 나온다고 문제에서 정해져 있으니까,
# 미리 0~40까지 저장할 리스트(즉, 표)를 만들어 둠
# count_zero[n]  : fibonacci(n)을 호출할 때 0이 출력되는 횟수
# count_one[n]   : fibonacci(n)을 호출할 때 1이 출력되는 횟수
count_zero = [0] * 41
count_one  = [0] * 41

# -------------------- 기본값 설정 (시작점) --------------------
# n이 0일 때 → fibonacci(0)은 '0'을 한 번 출력하고 끝남
count_zero[0], count_one[0] = 1, 0
# n이 1일 때 → fibonacci(1)은 '1'을 한 번 출력하고 끝남
count_zero[1], count_one[1] = 0, 1
# --------------------------------------------------------------

# -------------------- 규칙(점화식) 적용 부분 --------------------
# “점화식”이란: 이전 결과를 이용해서 다음 값을 구하는 규칙.
# 예) 피보나치 수열: f(n) = f(n-1) + f(n-2)
# 지금도 똑같이, n번째에서의 0과 1의 개수는
# 바로 전(n-1)과 그 전(n-2)에서 나온 횟수를 더한 값이 됨.
#
# 예를 들어,
# fibonacci(3)을 호출하면 내부적으로 fibonacci(2)와 fibonacci(1)을 호출하니까
# '0'과 '1'이 나온 횟수도 각각 그 둘을 더한 값이 되는 거야.
for i in range(2, 41):
    count_zero[i] = count_zero[i - 1] + count_zero[i - 2]
    count_one[i]  = count_one[i - 1] + count_one[i - 2]
# --------------------------------------------------------------

# -------------------- 결과 출력 --------------------
# 이제 표가 완성되었으니까, 입력된 n을 바로 넣어서 꺼내 쓰면 됨.
# 실제로 재귀 함수를 돌릴 필요 없이,
# 미리 계산해 둔 횟수를 바로 가져오기만 하면 빠르게 정답을 얻을 수 있음.
for _ in range(test):
    n = int(input())  # 예: 3
    print(count_zero[n], count_one[n])
# --------------------------------------------------------------



