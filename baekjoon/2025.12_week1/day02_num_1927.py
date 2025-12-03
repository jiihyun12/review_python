# 251203

import heapq      

inputn = int(input())  
heap = []         

for _ in range(inputn):
    x = int(input())  
    
    if x == 0:     
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)


# ==================================

import heapq      # 최소 힙 라이브러리

N = int(input())  # 연산의 개수
heap = []         # 실제로 값을 저장할 빈 힙 리스트

for _ in range(N):
    x = int(input())   # 입력 숫자 x
    
    if x == 0:
        # x가 0 → 가장 작은 값을 뽑아서 출력해야 한다.
        
        if heap:
            # 힙이 비어있지 않으면 최솟값 꺼내기
            print(heapq.heappop(heap))
        else:
            # 힙이 비어 있다면 0 출력
            print(0)
    else:
        # x가 0이 아닌 경우 → 힙에 삽입
        heapq.heappush(heap, x)

