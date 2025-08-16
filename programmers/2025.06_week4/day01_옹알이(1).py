# 250630

def solution(babbling):
    googoo = ["aya", "ye", "woo", "ma"]
    result = 0

    for i in babbling:
        word = i
        for sound in googoo:
            word = word.replace(sound, " ")  # 발음이 있으면 없애기
        if word.strip() == "":  # 다 발음 가능한 단어였다면!
            result += 1

    return result


# def 함수이름(매개변수):
#     실행할 코드
#     return 결과


# =======================================
# def solution(babbling):
# ‘babbling’이라는 단어 리스트를 받아서 발음 가능한 단어가 몇 개인지 세는 함수

# googoo = ["aya", "ye", "woo", "ma"]
# 아기가 발음할 수 있는 단어 목록

# result = 0
# 발음 가능한 단어 개수를 담은 변수
# 0으로 초기화

# for i in babbling
# babbling 리스트 안에 있는 단어들을 하나씩 꺼내서 
# 각 단어가 아기가 말할 수 있는 단어인지 확인

# word = i
# i는 원본 단어니까 바꿔 써도 되는 복사본 word를 하나 만든다.

# for sound in googoo
# 아기가 발음할 수 있는 단어들 하나씩 꺼내기

# word = word.replace(sound, " ")
# 그 발음이 word 안에 있으면 없애버려.
# 없애는 대신 공백(스페이스)으로 바꾼다.
# 예: "ayaye" → " ye" → " "

# if word.strip() == "":
# 모든 발음이 제거된 후, 남은 게 아무것도 없다면
# = 원래 단어는 전부 발음 가능한 단어로만 이루어져 있었던 것

# result += 1
# 그럼 발음 가능한 단어 1개 추가!

# return result
# 최종적으로 발음 가능한 단어가 몇 개인지 결과로 돌려주기
