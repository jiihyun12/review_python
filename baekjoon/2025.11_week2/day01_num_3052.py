# 251110

nums = set()

for _ in range(10):
    n = int(input())
    nums.add(n % 42)

print(len(nums))
