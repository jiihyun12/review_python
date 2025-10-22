# 251021

nums = [int(input()) for _ in range(9)]

m = max(nums)
idx = nums.index(m) + 1

print(m)
print(idx)

# ======================

리스트 컴프리헨션
한 줄로 리스트를 간결하게 만드는 문법
반복문 + append() 를 짧게 쓴 형태
[ 표현식 for 변수 in 반복가능객체 ]

nums = []
for _ in range(9):
    nums.append(int(input()))
-->
nums = [int(input()) for _ in range(9)]
-->
1) input()으로 숫자 입력받고 int()로 바꿈  
2) 그걸 리스트에 차곡차곡 넣음  
3) 총 9개 입력 → [3, 29, 38, 12, 57, 74, 40, 85, 61]



index()
: 리스트 안에서 원하는 값이 있는 첫 번째 위치(인덱스) 를 찾아주는 함수
리스트.index(찾을값)

m = max(nums)           # 최댓값 찾기
idx = nums.index(m) + 1 # 위치는 1부터 출력하라고 했으니까 +1


