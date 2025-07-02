# 250701

T = int(input())  

result = [] 

for i in range(T): 
    S = input()  
    result.append(S[0] + S[-1])  

for j in result:
    print(j) 

# ======================================

# T = int(input())
# 사용자가 입력할 문자열의 개수를 입력받는 부분

# result = []
# 결과를 저장할 빈 리스트를 만들어둠
# 결과값인 첫 글자 + 마지막 글자를 여기에 저장함

# for i in range(T):
# 문자열을 T번 입력받기 위해 반복

# S = input()
# 문자열을 한 줄 입력받는다.

# S[0] + S[-1]
# S[0]: 문자열의 첫 번째 문자
# S[-1]: 문자열의 마지막 문자

# result.append(...)
# 방금 구한 문자열을 result 리스트에 추가한다.

# for j in result: print(j)
# 리스트 안에 있는 값들을 하나씩 꺼내서 출력한다.