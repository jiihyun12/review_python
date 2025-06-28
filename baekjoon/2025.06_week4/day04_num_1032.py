# 250627_FRI

# 몇 개의 파일 이름이 주어질지 입력을 받고
n = int(input())

# 파일 이름들을 담을 리스트를 선언하고
filenames = []

# 파일 이름을 입력받고
for _ in range(n):
    name = input()
    filenames.append(name)


# 첫 번째 파일 이름 기준으로 패턴을 만들거야
# 1. 일단 파일 이름 길이를 받고
length = len(filenames[0])
# 2. 결과값 초기화(문자열로)
result = ""

# 각 위치별로 비교할거야
# 1. 현재 위치의 글자가 모두 같은지 확인하는 변수 선언
for i in range(length):
    same = True
    # 2. 첫 번째 파일의 i번째 문자 변수로 선언
    first_char = filenames[0][i]
    # 나머지 파일들과 i번째 글자를 비교해서 하나라도 다르면 비교를 중지한다.
    for j in range(1, n):
        if filenames[j][i] != first_char:
            same = False
            break
    if same:
        # 모두 같으면 해당 문자를 추가한다.
        result += first_char  
    else:
        # 하나라도 다르면 ?를 추가한다.
        result += '?'        

print(result)
