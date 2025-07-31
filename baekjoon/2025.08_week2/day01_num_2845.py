# 250813

L, P = map(int, input().split())
reuslt = L * P 
nums = list(map(int, input().split()))

for n in nums:
  print(n - reuslt, end = ' ')