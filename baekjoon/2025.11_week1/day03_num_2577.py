# 251105

A = int(input())
B = int(input())
C = int(input())

result = A * B * C         
result_str = str(result)    

for i in range(10):         
    print(result_str.count(str(i)))

# ================================

# (A×B×C)의 결과에 0~9 각 숫자가 몇 번 등장했는지 한 줄씩 출력

# 세 수를 입력 받고
# 곱한 결과를 문자열로 변환하고
# 0~9까지 돌면서 count()로 숫자를 센다.
