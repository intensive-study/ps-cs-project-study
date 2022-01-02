import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
bookpos = list(map(int, input().split()))
left, right = [], []
answer = 0
        
# 가장 먼 거리의 책을 마지막에 정리
maxpos = max(max(bookpos), -min(bookpos))

# 먼 거리부터 pop되도록 넣어줌
for pos in bookpos:
    if pos < 0:
        heapq.heappush(left, pos)
    else :
        heapq.heappush(right, -pos)


while left:
    answer -= heapq.heappop(left)
    for _ in range(M-1):
        if left : heapq.heappop(left)
        
while right:
    answer -= heapq.heappop(right)
    for _ in range(M-1):
        if right : heapq.heappop(right)

# 모두 왕복거리로 계산하고 가장 먼거리를 빼줌
print(2 * answer - maxpos)