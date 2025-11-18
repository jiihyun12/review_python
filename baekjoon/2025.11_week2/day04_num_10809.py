# 251114
s = input().strip()

for ch in 'abcdefghijklmnopqrstuvwxyz':
    print(s.find(ch), end=' ')


# ======================

# 알파벳 26개를 전부 순회 (chr() 또는 문자열 사용)
# 각 알파벳이 문자열에 존재하는지 확인
# 존재하면 **index()**로 첫 위치 찾기

# 존재하지 않으면 -1 출력


