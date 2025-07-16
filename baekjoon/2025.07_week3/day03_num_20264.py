# 250716

n = int(input())   

print(n * n)  
print(2)      

# ======================================

n = int(input())
A = [0] * (n + 1)  # A[1]부터 쓰려고 n+1 크기로 만듦

sum = 0

for i in range(1, n + 1):       # 바깥 for문 → n번
    for j in range(1, n + 1):   # 안쪽 for문 → n번
        sum += A[i] * A[j]      # 코드1 → 총 n²번 실행

print(n * n)  # 수행 횟수 = n²
print(2)      # 차수 = 2 (O(n²))

