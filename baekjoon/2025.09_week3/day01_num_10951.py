# 250914

while True:
    try:
        a,b = map(int, input().split())
        print(a + b)
    except:
        break


# ==================
# try 안에서 입력을 계속 받음
# 더 이상 입력이 없으면 EOFError가 발생 --> except에서 break
