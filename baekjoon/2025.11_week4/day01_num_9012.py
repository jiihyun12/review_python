# 251123

inputS = int(input())

for i in range(inputS):
    s = input().strip()
    count = 0
    ok = True

    for ch in s:
        if ch == '(':
            count += 1
        else: 
            count -= 1
            if count < 0:
                ok = False
                break

    if count != 0:
        ok = False

    print("YES" if ok else "NO")


# ===============================

# ( 만나면 count += 1
# ) 만나면 count -= 1

# 근데 여기서 count가 음수가 되면?
# 닫는 괄호가 먼저 나온 거라서 실패!

# 문자열 다 돌았는데 count == 0
# 제대로 다 닫힌 거라 YES
# 아니면 NO

