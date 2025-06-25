#250621

x = int(input())
y = int(input())

if(x > 0 and y > 0):
    print(1)
elif(x < 0 and y > 0):
    print(2)
elif(x < 0 and y < 0):
    print(3)
elif(x > 0 and y < 0):
    print(4) 


# ===========================

# 오답 노트

# x = input() --> input으로 받은 값은 기본적으로 str이기 때문에 int로 변환 필요
# y = input()

# if(x > 0 && y > 0) --> 파이썬에서는 &&가 아닌 and , 조건문 뒤에는 :
#     print(1)
# elif(x < 0 && y > 0)
#     print(2)
# elif(x < 0 && y < 0)
#     print(3)
# elif(x > 0 && y < 0)
#     print(4) 