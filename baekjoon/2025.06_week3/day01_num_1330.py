#250620

# 오른쪽 마우스 클릭 → Run Python File in Terminal

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")