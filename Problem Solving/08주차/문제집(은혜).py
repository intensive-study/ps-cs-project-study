import heapq

n, m = map(int, input().split())
seq = [[] for i in range(n+1)] 
indegree = [0] * (n+1) 
heap = [] 
rslt = [] 

for _ in range(m):
    a, b = map(int, input().split())
    seq[a].append(b)
    indegree[b] += 1

# 차수가 0인 문제를 추가(바로 풀 수 있는 문제)
for i in range(n):
    if indegree[i+1] == 0:
        heapq.heappush(heap, i+1)
        
while heap:
    data = heapq.heappop(heap)
    rslt.append(data)
    for b in seq[data]:
        indegree[b] -= 1
        if indegree[b] == 0:
            heapq.heappush(heap, b)

print(*rslt)