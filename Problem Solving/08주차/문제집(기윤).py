import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
adj = [[] for _ in range(n+1)]
pq = []
answer = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    adj[a].append(b)

for i in range(1, n+1):
    if not indegree[i]: heappush(pq, i)

for i in range(1, n+1):
    if not pq: break
    x = heappop(pq)
    answer[i] = x

    for nx in adj[x]:
        indegree[nx] -= 1
        if not indegree[nx]: heappush(pq, nx)
    
print(*answer[1:])