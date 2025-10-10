# 251003

import sys
input = sys.stdin.readline

N = int(input())

times = list(map(int, input().split()))

times.sort()

total = 0      
current = 0    

for t in times:
    current += t    
    total += current  

print(total)

# ============================
