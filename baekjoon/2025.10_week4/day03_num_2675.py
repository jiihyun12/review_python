# 251022

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = ''
    for c in S:
        result += c * R
    print(result)
