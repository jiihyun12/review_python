# 250915

# 단어들을 중복 제거한 뒤, 길이 오름차순 → 사전순으로 정렬

import sys
input = sys.stdin.readline  # 많은 줄 빠르게 읽기

n = int(input().strip())

words = set()               # 중복 제거용 (집합)
for _ in range(n):
    w = input().strip()
    words.add(w)            # 동일 단어가 여러 번 나와도 1개만 남음

# 정렬 기준:
# 1) len(w) 오름차순
# 2) 길이가 같으면 w(사전순) 오름차순
sorted_words = sorted(words, key=lambda w: (len(w), w))

# 한 줄에 하나씩 출력
print("\n".join(sorted_words))
