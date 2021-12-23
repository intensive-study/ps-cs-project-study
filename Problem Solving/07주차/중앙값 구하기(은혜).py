import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):    
    size = int(input())
    xlist = []
    for _ in range(int((size-1) / 10) + 1):
        xlist.extend(map(int, input().split()))
        
    left_heap = [(-xlist[0], xlist[0])]
    right_heap = []
    answer = [xlist[0]]
    
    for x in xlist[1:]:
        # right heap의 최소보다 크면 right heap에 넣고 갯수 맞는지 확인
        if len(right_heap) > 0 and right_heap[0][1] < x:
            heapq.heappush(right_heap, (x, x))            
            if len(right_heap) > len(left_heap):#불가능한 상태(left가 right보다 크거나 같을 수 밖에 없음)
                x = heapq.heappop(right_heap)[1]
                heapq.heappush(left_heap, (-x, x))
        # 그렇지 않으면 무조건 left heap에 넣고 갯수 맞는지 확인
        else:
            heapq.heappush(left_heap, (-x, x))            
            if len(left_heap) > len(right_heap) + 1: #불가능한 상태(left가 right보다 1 크거나 같을 수 밖에 없음)
                x = heapq.heappop(left_heap)[1]
                heapq.heappush(right_heap, (x, x))           
                    
        if len(left_heap) > len(right_heap):
            answer.append(left_heap[0][1])
            
    print(len(answer))
    for i, a in enumerate(answer):
        if i!= 0 and i % 10 == 0:
            print()
        print(a, end =" ")
    print()
        