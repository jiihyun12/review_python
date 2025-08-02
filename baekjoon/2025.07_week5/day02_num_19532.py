# 250802


a, b, c, d, e, f = map(int, input().split())

isFound = False

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)

            isFound = True
            break 
    
    if isFound:
        break

# ========================================

# a, b, c, d, e, f --> 입력으로 주어지는 정수
# x와 y는 우리가 찾아야 하는 정수 해

# 문제 조건:
# 해 (x, y)는 항상 정수
# −999≤x,y≤999

# 예시
# 1 3 -1 4 1 7

# 1x+3y=−1
# 4x+1y=7

# y=−1
# x=2

# 2 -1



# a, b, c, d, e, f = map(int, input().split()) #문제에서 주는 여섯 개 정수를 한 줄에서 입력받아 각각 저장

# isFound = False  # 정답 찾았는지 여부 저장 아직 (x, y)를 못 찾았으니 False로 시작

# for i in range(-999, 1000):  # x 후보 전부 (-999 ~ 999) i -> x후보. 범위는 문제 조건대로 -999부터 999까지 전부 확인
#     for j in range(-999, 1000):  # y 후보 전부 (-999 ~ 999) j -> y후보. 역시 -999부터 999까지 전부 확인

#         # 두 식이 모두 만족하는지 확인
#         if (a*i) + (b*j) == c and (d*i) + (e*j) == f: 
            # 첫 번째 식: a⋅i+b⋅j=c
            # 두 번째 식: d⋅i+e⋅j=f
            # 두 조건이 모두 맞으면 (i, j)가 해

#             print(i, j)  # 정답 출력 (해를 출력)
#             isFound = True  # 찾았다고 표시 isFound = True로 변경 
#             break  # y 반복문 중단 안쪽 for(y 반복) 탈출
    
#     if isFound:  # 이미 찾았으면
#         break  # x 반복문도 중단  이미 해를 찾았으니 바깥 for(x 반복)도 종료
