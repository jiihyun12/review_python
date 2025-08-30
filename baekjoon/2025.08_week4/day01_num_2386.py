# 250830

while True:
    n = input()

    if n == '#' :
        break

    target = n[0].lower()
    sentence = n[2:].lower()
    count = sentence.count(target)

    print(n[0], count)


#--------------------------------------

# while True:
# 입력을 한 줄씩 계속 받는다.

# n = input()
# 한 줄 통째로 읽는다. 예) "a Apple and banana"

# if n == '#': break
# 입력이 #면 종료(문제의 종료 조건).

# target = n[0].lower()
# 첫 글자(찾을 알파벳)를 소문자로 변환해서 저장.
# → 대소문자 구분 없이 세기 위해

# sentence = n[2:].lower()
# 인덱스 1에는 공백이 온다는 형식을 가정하고, 2번째 문자부터 끝까지(문장 부분)를 소문자로 저장.

# count = sentence.count(target)
# 문장 속에 target 문자가 몇 번 나오는지 센 값.

# print(n[0], count)
# 원래 입력 첫 글자(대소문자 보존)와 개수를 출력.