# 250704

word = input()
same = True

i = 0

while i < len(word) // 2:
    front = word[i]
    back = word[len(word) -1 -i]

    if front != back:
        same = False
        break
    i = i + 1

if same == True:
    print(1)
else:
    print(0)



# ==================================

# 1. 사용자로부터 문자열을 입력받는다.
# word = input()
# 사용자가 키보드로 단어를 입력하면 word에 저장
# 예: 사용자가 level이라고 입력하면 word = "level"

# 2. 처음엔 "글자가 모두 같다"라고 가정하고 시작한다.
# same = True
# 이 변수는 True(같다), False(다르다) 중 하나의 값을 가질 것
# 처음엔 "모두 같을 것이다" 라고 생각하고 True로 시작한다.

# 3. 비교 시작: 앞과 뒤를 차례로 비교할 준비
# i = 0
# i는 몇 번째 글자를 보고 있는지를 나타낸다.
# 처음엔 0 → 즉, 첫 번째 글자부터 비교 시작

# 4. 전체 글자의 절반까지만 비교한다.
# while i < len(word) // 2:
# 예: word = "level"이면 길이는 5 → 5 // 2 = 2
# i = 0일 때 → word[0] vs word[4]
# i = 1일 때 → word[1] vs word[3]
# 중앙 글자 word[2]는 비교 안 해도 된다. 혼자니까

# if front != back:
#         same = False
#         break
# 앞과 뒤가 다르면 same = False로 바꾸고
# 더 이상 비교할 필요 없으니 break로 반복문 종료

#  i = i + 1
# 다음 글자로 넘어가기 위한 준비

# 5. 다 비교한 뒤 결과 출력
# if same == True:
#     print(1)
# else:
#     print(0)
# same == True → 모든 앞/뒤 글자가 같았으므로 팰린드롬 → 1 출력
# same == False → 하나라도 다르면 팰린드롬 아님 → 0 출력