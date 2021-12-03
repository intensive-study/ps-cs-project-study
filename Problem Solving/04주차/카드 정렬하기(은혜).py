import sys
import heapq

N = int(sys.stdin.readline())
hq = []
answer = 0

for _ in range(N):
    heapq.heappush(hq, int(sys.stdin.readline()))
    
while len(hq) > 1 :
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    answer += (a + b)
    heapq.heappush(hq, a+b)
    
print(answer)