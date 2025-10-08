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






