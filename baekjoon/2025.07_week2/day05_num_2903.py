# 250711

# 어떤 패턴에 따라 점들이 늘어난다.
# N번 반복하면 점이 몇 개 생기는지를 구하는 문제

# 반복 횟수 N을 입력받고
# 처음에는 2×2 점 (한 변에 2개)
# 매 반복마다 한 변의 점 개수 = 이전의 * 2 - 1
# 마지막에 전체 점 개수 = 한 변 점 개수 × 한 변 점 개수

N = int(input()) 
point = 2  

for i in range(N):
    point = point * 2 - 1  
print(point * point)  


# ===================================

N = int(input())  # 반복 횟수 입력

point = 2  # 처음 한 변에 점 2개

for _ in range(N):
    point = point * 2 - 1  # 한 번 이동하면 점이 사이사이에 생김

print(point * point)  # 전체 점 개수는 정사각형이니까 제곱





