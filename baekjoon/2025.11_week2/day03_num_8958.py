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


