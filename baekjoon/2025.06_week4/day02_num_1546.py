#250625_WED

N = int(input())
scores = list(map(int, input().split()))  # 리스트로 변환

max_score = max(scores)  # 최대 점수 구하기

# 점수 변환: (점수 / 최고점수) * 100
new_scores = [(s / max_score) * 100 for s in scores]

# 평균 계산
average = sum(new_scores) / N

print(average)


# =========================

# 오답 노트
# N = int(input())
# score = map(int, input().split())  # score는 map 객체 → 한 번만 순회 가능

# max_score = max(score)  # 여기서 map이 소비됨
# result_score = (score / max_score) * 100  # score는 더 이상 값 없음, 연산 불가

