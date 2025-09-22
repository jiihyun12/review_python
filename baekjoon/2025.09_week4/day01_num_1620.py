# 250922

import sys
input = sys.stdin.readline

# N: 포켓몬 개수, M: 문제 개수
N, M = map(int, input().split())

# 번호 → 이름 (인덱스 1부터 시작, 편의를 위해 크기 N+1)
num_to_name = [None] * (N + 1)

# 이름 → 번호 (빠른 검색을 위해 딕셔너리 사용)
name_to_num = {}

# 도감에 포켓몬 등록
for i in range(1, N + 1):
    name = input().strip()   # 포켓몬 이름
    num_to_name[i] = name    # 번호로 찾기
    name_to_num[name] = i    # 이름으로 찾기

out = []  # 출력 결과를 모아뒀다가 한 번에 출력 (속도 개선)

# 질문 처리
for _ in range(M):
    q = input().strip()
    if q.isdigit():   # 질문이 숫자라면 (번호 → 이름)
        out.append(num_to_name[int(q)])
    else:             # 질문이 문자라면 (이름 → 번호)
        out.append(str(name_to_num[q]))

# 결과 출력
print("\n".join(out))



# ==============================

# 포켓몬 도감: 총 N개 포켓몬, 각 포켓몬은 번호와 이름을 동시에 가짐

# M개의 질문이 주어짐:
# 숫자가 들어오면 해당 번호의 포켓몬 이름 출력
# 이름이 들어오면 해당 포켓몬 번호 출력

