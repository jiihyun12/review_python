# 250706

n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))
nums.sort()

for num in nums:
    print(num)


# 입력수가 최대 100만개이므로 input을 그냥 쓰면 느려서 시간 초과가 날 수 있다.
import sys

n = int(sys.stdin.readline())

nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)


# ========================

# 첫 줄에서 정수 하나 입력받고, 그것을 n에 저장한다.
# --> 이 n은 '입력받을 숫자의 개수'를 의미한다.
n = int(input())

# 비어 있는 리스트를 만든다.
# --> 여기에 입력받은 숫자들을 하나씩 저장할 것!
nums = []

# n번 반복하면서 정수를 입력받아 nums 리스트에 추가한다.
# --> input()으로 입력받고, int()로 정수로 바꿔서 리스트에 넣는다.
for _ in range(n):
    nums.append(int(input()))

# 리스트에 있는 모든 숫자를 오름차순으로 정렬한다.
# --> sort()는 리스트 자체를 직접 정렬해준다.
nums.sort()

# 정렬된 숫자들을 하나씩 꺼내서 출력한다.
# --> for문으로 리스트 안의 숫자들을 순서대로 하나씩 출력한다.
for num in nums:
    print(num)
