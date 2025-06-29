# 250629

n = int(input())

count = 0  # 봉지 개수

while n >= 0:
    if n % 5 == 0:
        count += n // 5  # 남은 건 전부 5kg 봉지로
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)  # 딱 맞게 안 나눠질 경우


# =================================

# 18은 5로 안 나눠짐 --> 3 빼고 count +1 --> n=15
# 15는 5로 나눠짐 --> count += 15 // 5 = 3
# 총 count = 1(3kg) + 3(5kg) = 4봉지

# n % 5 == 0	남은 무게가 5로 딱 나눠질 수 있다면
# n -= 3	3kg 봉지 하나 쓰고 다시 시도
# while n >= 0	0kg까지는 시도해볼 수 있음
# else: print(-1)	끝까지 안 맞으면 실패 처리