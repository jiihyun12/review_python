# 251020

A, B = map(int, input().split())
cnt = 1

while B > A:
    if B % 10 == 1:   
        B //= 10
    elif B % 2 == 0:  
        B //= 2
    else:            
        break
    cnt += 1

print(cnt if A == B else -1)

# =========================

# A, B = map(int, input().split())
# cnt = 1

# while B > A:
#     if B % 10 == 1:   # 끝이 1이면 → 뒤 1 제거
#         B //= 10
#     elif B % 2 == 0:  # 짝수면 → 반으로 나누기
#         B //= 2
#     else:             # 둘 다 안 되면 실패
#         break
#     cnt += 1

# print(cnt if A == B else -1)


# A, B = map(int, input().split())	
# 시작값 A, 목표값 B 입력

# cnt = 1	
# 연산 횟수(자기 자신 포함)

# while B > A:	
# B가 A보다 클 동안 반복 (줄이기 진행)

# if B % 10 == 1:	
# 끝자리가 1이면, //10으로 1을 제거

# elif B % 2 == 0:	
# 짝수면, 2로 나누기

# else: break
# 둘 다 안 되면 더 이상 줄일 수 없음

# cnt += 1	
# 한 번 줄였으니까 연산 횟수 +1

# print(cnt if A == B else -1)	
# A로 정확히 도달했으면 cnt, 아니면 -1