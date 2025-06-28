# 250621

point = int(input())

if(90 <= point <= 100):
    print("A")

elif(80 <= point < 90):
    print("B")

elif(70 <= point < 80):
    print("C")

elif(60 <= point < 70):
    print("D")
    
else:
    print("F")



# =====================================================================

# 오답 노트

# point = map(int, input().split()) --> map으로 하면 여러 개 입력받는 것. 점수는 하나니까 map 아님

# if(90 >= point >= 100): --> 조건 순서를 반대로 작성함
# print("A") --> 들여쓰기 안 함

# elseif(80 > point > 90): --> 파이썬에서는 elif 사용
# print("B")

# elseif(70 > point > 80):
# print("C")

# else:
# print("F")