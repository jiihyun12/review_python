# 2500708

# 9×9 크기의 정수 배열이 주어짐
# 이 배열에서 최댓값을 찾고
# 그 최댓값의 행 번호, 열 번호(1부터 시작!)를 출력


# 전체 9×9 배열에서 최댓값 찾기
# 그 위치를 1부터 시작하는 좌표로 출력

max_num = -1
max_row = 0
max_col = 0

row_num = 1

while row_num <= 9:
    line = input().split()

    col_num = 1

    for num in line: 
        num = int(num)

        if num > max_num:
            max_num = num
            max_row = row_num
            max_col = col_num

        col_num += 1  

    row_num += 1 

print(max_num)
print(max_row, max_col)

# ========================================
# 지금까지 입력받은 숫자 중 가장 큰 값을 저장할 변수
# 처음에는 -1로 시작 (모든 입력은 0 이상이므로 무조건 바뀌니까)
max_num = -1

# 최댓값이 나타난 행(줄) 번호를 저장할 변수.
max_row = 0

# 최댓값이 나타난 열(칸) 번호를 저장할 변수
max_col = 0

# 현재 몇 번째 줄(행)을 입력 중인지 추적하는 변수
# 문제는 1행부터 9행까지 있으므로 1부터 시작
row_num = 1

# 총 9줄을 입력받아야 하므로 while문을 9번 반복
while row_num <= 9:
    
    # 한 줄에 있는 9개의 숫자를 문자열로 입력받고 공백 기준으로 나눈 후 문자열 리스트로 저장
    # 예: '3 4 5 6 ...' → ['3', '4', '5', ...]
    line = input().split()

    # 현재 줄의 몇 번째 칸(열)을 보는지 추적하는 변수
    # 문제는 1열부터 9열까지 있으므로 1부터 시작
    col_num = 1

    # line 리스트 안의 숫자들을 하나씩 순회하며 확인
    for num in line: 
        # 문자열 상태의 숫자를 정수형으로 바꾼다.
        num = int(num)

        # 지금 보고 있는 숫자가 현재까지의 최댓값보다 크다면
        if num > max_num:
            # 최댓값을 새로 저장하고
            max_num = num
            # 그 숫자가 있는 행과 열의 위치도 같이 저장
            max_row = row_num
            max_col = col_num

        # 다음 칸(열)로 이동하기 위해 열 번호를 1 증가
        col_num += 1  

    # 한 줄 처리가 끝났으니까 다음 줄(행)로 넘어가기 위해 행 번호 증가
    row_num += 1 

# 모든 숫자를 다 확인했으니까 최댓값을 출력
print(max_num)

# 최댓값이 있는 위치 (행, 열)을 출력
# 문제는 1부터 시작하는 좌표를 요구하므로 그대로 출력
print(max_row, max_col)

