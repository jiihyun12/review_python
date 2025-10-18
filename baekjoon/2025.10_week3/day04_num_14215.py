# 251018

a, b, c = sorted(map(int, input().split()))  

if a + b > c:
    print(a + b + c)            
else:
    print(2 * (a + b) - 1)       

