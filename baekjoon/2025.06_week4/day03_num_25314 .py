# 250626_THU

n = int(input())  # 사용자로부터 정수 입력 받기
count = n // 4    # 문제 조건: n은 4의 배수이며, n / 4 만큼 "long"을 반복하는 것

l_long = "long "
i_int = "int" # 마지막에 붙일 "int" 문자열을 따로 변수에 저장
result = ""

for i in range(count):  # long을 count번 반복 
    result += l_long

result += i_int # 반복이 끝난 뒤 "int"를 마지막에 붙인다.

print(result)

