# 251006

N = input()
sep = N.split("-")

def sum_something(i):
    return sum(int(x) for x in i.split('+') if x)

result = sum_something(sep[0]) - sum(sum_something(y) for y in sep[1:])

print(result)

# ====================================

# 입력받은 문자열을 - 기준으로 나눔
N = input()
sep = N.split("-")

# + 기준으로 나누고, 각 항을 int()로 바꿔 더함
def sum_something(i):
    return sum(int(x) for x in i.split('+') if x)

# 첫 덩어리(sep[0])는 그대로 더하고
# 나머지 덩어리(sep[1:])는 전부 더한 뒤 전부 빼버림
result = sum_something(sep[0]) - sum(sum_something(y) for y in sep[1:])

print(result)


