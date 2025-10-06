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

#1️. sep[0] = '55'
# sum_something('55') = 55
# 첫 번째 조각은 그냥 더한다.
# 2️. sep[1:] = ['50+40']
# 각 조각마다 sum_something()을 적용해서 전부 더한다.
# sum(sum_something(y) for y in sep[1:]) = 90
# 뒤의 조각들은 모두 빼버린다.

#수학적으로 괄호를 넣을 수 있는 방법 중 결과가 최소가 되게 하려면
# 첫 - 이후에 나오는 건 전부 하나로 묶어서 빼는 게 제일 작게 나오기 때문에 이렇게 한다.
print(result)


