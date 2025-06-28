#250625_WED

x = int(input()) # 영수증에 적힌 총 지불 금액을 입력받아 정수로 저장
n = int(input()) # 구매한 물건 종류 수 입력

total = 0 # 총합을 계산하기 위한 초기값 설정

for i in range(1, n+1):  # 물건 종류 수만큼 반복 (1부터 n까지)
    a,b = map(int, input().split())  # 각 줄에서 가격 a, 개수 b를 정수로 입력받음
    total += a * b  # 개당 가격 × 개수 → 그 값을 누적해서 총합에 더함
    
if(total == x):  # 계산한 총합과 처음에 입력받은 총 금액이 같은지 비교
    print("Yes")  # 같으면 "Yes" 출력
else :
    print("No")  # 	다르면 "No" 출력

