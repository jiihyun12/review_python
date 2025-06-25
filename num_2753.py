# 2753

day = int(input())
leap_day = (day % 4 == 0 and day % 100 != 0) or day % 400 == 0

if(leap_day):
    print(1)
else:
    print(0)


# ===========================================================

# 오답 노트

# day = int(input())
# leap_day = day % 4 == 0 and day % 100 != 0 and day % 400 == 0
# --> 4의 배수이고 100의 배수는 아니고 400의 배수이다라고 잘못 표기
#     조건은 4의 배수이면서 100의 배수가 아니거나 400의 배수여야함

# if(leap_day):
#     print(1)
# else:
#     print(0)