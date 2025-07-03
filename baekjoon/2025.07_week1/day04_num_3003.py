# 250703

nums = [1,1,2,2,2,8]
count = list(map(int, input().split()))
reuslt = []

for i in range(6):
    reuslt.append(nums[i] - count[i])
print(*reuslt)

# ===========================

# nums --> 킹~폰까지의 원래 개수
# count --> 입력받은 현재 개수 (리스트로 변환)
# result.append(...) --> 개수 차이를 리스트에 저장하기
# *result --> 리스트를 공백으로 나눠서 출력한다. 
#             파이썬에서 * 기호는 언패킹(unpacking) 기능을 갖는다.
#             묶여 있는 자료(리스트, 튜플 등)의 요소들을 풀어헤쳐서 꺼내주는 것이다.