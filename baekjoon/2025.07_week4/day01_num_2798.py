# 250721

N, M = map(int, input().split()) 
item = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (item[i] + item[j] + item[k]) <= M:
                result = max(result, (item[i] + item[j] + item[k]))

print(result)

 # ========================================

N, M = map(int, input().split())  
# 첫 번째 줄 입력받기  
# N = 카드 개수, M = 넘지 말아야 하는 합계  

item = list(map(int, input().split()))  
# 두 번째 줄 입력받기  
# 카드에 적힌 숫자들을 리스트로 저장  

result = 0  
# 최댓값을 담을 변수 초기화  

for i in range(N):  
    for j in range(i+1, N):  
        for k in range(j+1, N):  
            # i, j, k가 모두 다른 카드 인덱스  
            if (item[i] + item[j] + item[k]) <= M:  
                # 세 카드의 합이 M 이하일 때만  
                result = max(result, (item[i] + item[j] + item[k]))  
                # 현재 result와 비교해서 더 큰 값으로 갱신  

print(result)  
# 최종 최댓값 출력



