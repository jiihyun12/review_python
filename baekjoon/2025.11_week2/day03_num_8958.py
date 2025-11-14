# 251112

T = int(input()) 

for _ in range(T):
    s = input().strip()  
    score = 0             
    count = 0             

    for ch in s:
        if ch == 'O':
            count += 1       
            score += count    
        else:
            count = 0        

    print(score)


# ==========================

# 문자열을 왼쪽부터 순회
# O면 count += 1
# X면 count = 0 (초기화)
# 매번 total += count

