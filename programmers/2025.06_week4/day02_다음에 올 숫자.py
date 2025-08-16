# 250702

def solution(common):
    a = common[0]  # 첫 번째 숫자
    b = common[1]  # 두 번째 숫자
    c = common[2]  # 세 번째 숫자

    # 등차수열인지 확인 (두 수 차이가 똑같니?)
    if b - a == c - b:
        d = b - a  # 공차
        return common[-1] + d
    else:
        r = b // a  # 공비
        return common[-1] * r

# =============================================
# 앞에서 두 개 숫자 뺀 거랑, 그 다음 두 개 뺀 게 똑같으면 등차수열
# 아니면 곱한 거니까 등비수열