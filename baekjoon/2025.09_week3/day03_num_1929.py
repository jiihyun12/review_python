# 250916

# 주어진 구간 [M, N]안의 모든 소수 출력

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0], is_prime[1] = False, False

p = 2
while p * p <= N:
    if is_prime[p]:
        for multiple in range( p * p, N + 1, p):
            is_prime[multiple] = False
    p += 1

for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
 

# 에라토스테네스의 체
# 2부터 시작해서 자기 자신을 제외한 배수를 모두 지움.
# 다음 남아 있는 수를 찾아서, 그 수의 배수도 모두 지움.
# 이 과정을 √N 이하까지 반복하면, 지워지지 않고 남아 있는 수들이 모두 소수

M, N = map(int, input().split())

# 소수 여부를 저장하는 리스트 (True = 소수)
is_prime = [True] * (N + 1)
is_prime[0], is_prime[1] = False, False  # 0, 1은 소수가 아님

# 2부터 √N 까지만 확인
p = 2
while p * p <= N:
    if is_prime[p]:
        # p의 배수들을 False 처리 (p*p부터 시작하면 됨)
        for multiple in range(p * p, N + 1, p):
            is_prime[multiple] = False
    p += 1

# M 이상 N 이하의 소수 출력
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
