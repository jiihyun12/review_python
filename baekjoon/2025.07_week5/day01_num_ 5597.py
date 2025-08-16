# 250728

# 총 학생 수: 30명 
# 과제 제출 학생 수: 28명
# 찾아야 할 것: 과제를 제출하지 않은 2명의 학생 번호

# 모든 학생 리스트 만들기: 1번부터 30번까지의 숫자를 가진 리스트를 하나 만들고
students = []
for i in range(1, 31):
    students.append(i)
# 제출 학생 번호 입력받기: 과제를 제출한 28명의 학생 번호를 하나씩 입력받는다.
for _ in range(28):
    input_students = int(input())
# 제출 학생 번호 제거하기: 전체 학생 리스트에서 입력받은 제출 학생 번호들을 하나씩 지우면
    students.remove(input_students)
# 남은 학생 번호 출력하기: 리스트에 남아있는 번호가 과제를 제출하지 않은 학생 번호!
students.sort() # 오름차순

for students_numbers in students:
    print(students_numbers)    
    

# =========================================

# all_students = list(range(1, 31))
# range(1, 31)은 1부터 30까지의 숫자를 만들어준다.
# list()로 이걸 리스트로 바꿔서 all_students에 저장한다.'
# 이제 all_students는 [1, 2, 3, ..., 30] 이렇게 되어있음

# for _ in range(28):
# 이 부분은 28번 반복하라는 뜻
# 과제 제출한 학생이 28명이니까 28번 입력받을  것
# _ 는 반복 횟수만 중요하고, 변수에 저장할 필요가 없을 때 관례적으로 사용한다.

# submitted_student = int(input())
# input()은 키보드로 숫자를 입력받는 것
# 예를 들어, 3번 학생이 제출했으면 3을 입력한다.
# int()는 입력받은 글자를 숫자로 바꿔준다.

# all_students.remove(submitted_student)
# all_students 리스트에서 submitted_student에 해당하는 숫자를 지워버린다. 
# 만약 3번을 입력했다면, 리스트에서 숫자 3이 사라지는 것

# all_students.sort()
# 과제를 제출하지 않은 두 학생 번호가 남아있을 텐데, 
# 문제에서는 작은 번호부터 출력하라고 했으니, sort()를 쓰면 숫자들이 작은 것부터 큰 것 순서대로 예쁘게 정렬됨

# for student_number in all_students:
# 이제 all_students 리스트에는 과제를 안 낸 학생 번호 두 개만 남아있다.
# 이 for문으로 리스트에 남은 각각의 학생 번호를 하나씩 print()로 출력한다.


