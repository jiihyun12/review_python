# 250922

# 리스트 nums = [3, 8, 11, 4, 9, 2]에서 짝수만 골라 2배 한 값을 새 리스트에 담아 출력
# 원본 리스트는 수정하지 말 것
# for 반복문과 append()만 사용 (리스트 컴프리헨션/filter 금지)

nums = [3, 8, 11, 4, 9, 2]
arr1 = []

for i in nums:
    result = i * 2
    if i % 2 == 0:
        arr1.append(result)
print(arr1)


