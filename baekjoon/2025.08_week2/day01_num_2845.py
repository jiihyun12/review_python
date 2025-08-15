# 250813

# 기자들이 5개의 기사에서 참석자 수를 썼는데, 실제 참석자수와 비교했을 때 얼마나 차이가 나는지?

L, P = map(int, input().split())
reuslt = L * P 
nums = list(map(int, input().split()))

for n in nums:
  print(n - reuslt, end = ' ')

