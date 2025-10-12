# 251012

N = int(input())

for i in range(1, N + 1):  # 1부터 N까지 반복 
    print("*" * i)  # i번째 줄에서는 별을 i개 출력

# =========================

N = int(input())
line = ""
for _ in range(N):
    line += "*"   # 한 개씩 누적
    print(line)   # 누적된 만큼 출력
