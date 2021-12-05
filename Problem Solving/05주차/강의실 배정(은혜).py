import heapq
import sys
import heapq

input = sys.stdin.readline
N = int(input())
lessons = [list(map(int, input().split())) for _ in range(N)]
hq = []

# 시작시간 빠른 순 정렬
lessons = sorted(lessons, key = lambda x : x[0])

#시작시간이 빠른 수업의 끝나는 시간을 hq에 담고 
# 끝나는 시간이 빠른 레슨과 그다음 시작시간을 비교함.
for lesson in lessons:
    if hq and hq[0] <= lesson[0]:
        heapq.heappop(hq)
    heapq.heappush(hq, lesson[1])
    
print(len(hq))