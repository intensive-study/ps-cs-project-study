import sys
import heapq
n = int(sys.stdin.readline())
left_heap = []
right_heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    #[-99, 1, 2, 5] / [5, 7, 10]
    if i % 2 == 0:
        if i != 0 and x > right_heap[0][1]: #right_heap 값 존재하면서 left에 들어갈 값이 right 최소보다 클때
             heapq.heappush(right_heap, (x, x))
             x = heapq.heappop(right_heap)[1]
        heapq.heappush(left_heap, (-x, x))
    else:
        if left_heap[0][1] > x: # right에 들어갈 값 x가 left_heap의 최대보다 작을 때
             heapq.heappush(left_heap, (-x, x))
             x = heapq.heappop(left_heap)[1]
        heapq.heappush(right_heap, (x, x))
        
    print(">>",left_heap[0][1])
    
    
