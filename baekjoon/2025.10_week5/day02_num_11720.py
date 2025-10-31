# 251031

N = int(input().strip())
s = input().strip()
result = 0
for ch in s:
    result += int(ch)
print(result)


# ========================================

N = int(input().strip())   # 숫자의 개수 입력 (사용은 안 해도 무방)
s = input().strip()        # 공백 없이 붙은 숫자 문자열 입력
result = 0                 # 합계를 저장할 변수 초기화

for ch in s:               # 문자열을 한 글자씩 순회
    result += int(ch)      # 각 문자를 정수로 변환해 더함

print(result)              # 최종 결과 출력
