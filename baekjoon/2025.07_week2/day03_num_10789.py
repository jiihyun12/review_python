# 250709

# 총 5줄의 문자열이 주어집니다.
# 각 줄의 길이는 서로 다를 수 있어요 (최대 15자).
# 이 문자열들을 세로로 읽어서 출력합니다.

words = []
result = ''

for _ in range(5):
    words.append(input())
    
for i in range(15):  
    for j in range(5):  
        
        if i < len(words[j]):
            result += words[j][i]

print(result)


# =================================

# 입력은 5줄
# 각 줄은 최대 15글자
# 첫 번째 글자들끼리, 두 번째 글자들끼리, ... 세로로 읽기
# 없는 글자는 무시


# 5줄의 문자열을 리스트에 저장
words = []

for _ in range(5):
    words.append(input())

# 결과를 담을 빈 문자열
result = ''

# 세로로 읽으려면 글자 위치(0부터 14까지)를 기준으로 반복
for i in range(15):  # 각 열(문자 위치)
    for j in range(5):  # 각 줄(행)
        # 만약 j번째 줄의 길이가 i보다 크다면,
        # 즉, 그 위치에 글자가 존재하면
        if i < len(words[j]):
            # 그 글자를 결과에 추가
            result += words[j][i]

# 마지막에 결과 출력
print(result)


# words[j][i]는 j번째 줄의 i번째 글자
# 그런데 어떤 줄은 글자가 짧을 수 있으니까 if i < len(words[j])로 검사 먼저 한다.
# 그 글자가 있으면 result에 붙인다.