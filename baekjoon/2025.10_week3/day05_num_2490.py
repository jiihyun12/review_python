# 251019

mp = {0: 'E', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}

for _ in range(3):
    zeros = list(map(int, input().split())).count(0)
    print(mp[zeros])

