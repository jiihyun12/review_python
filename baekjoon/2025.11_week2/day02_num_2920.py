# 251111

nums = list(map(int, input().split()))

if nums == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif nums == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")


# =================================

# 한 줄로 8개의 숫자를 입력받음
# 정수 리스트로 변환
# [1,2,3,4,5,6,7,8] 과 같은지 비교
# [8,7,6,5,4,3,2,1] 과 같은지 비교
# 둘 다 아니면 mixed