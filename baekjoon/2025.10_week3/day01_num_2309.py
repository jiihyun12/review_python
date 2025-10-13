# 251013

# 난쟁이는 9명이고, 각각의 키가 주어짐
# 그중 7명만 진짜 난쟁이이고, 그들의 키 합은 100

# 9명 중 2명만 가짜이고
# 그 두 명을 찾아서 제외한 뒤
# 남은 7명의 키를 오름차순으로 출력

heights = [int(input().strip()) for _ in range(9)]

total = sum(heights)
need = total - 100

seen = set()
fake_a = None
fake_b = None

for h in heights:
    complement = need - h
    if complement in seen:
        fake_a = h
        fake_b = complement
        break
    seen.add(h)

answer = heights[:]
answer.remove(fake_a)
answer.remove(fake_b)

for x in sorted(answer):
    print(x)