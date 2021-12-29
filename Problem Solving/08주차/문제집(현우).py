import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
heap = []
indegree = [0] * (N+1)
arr = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    arr[a].append(b)
for i in range(1,N+1):
    arr[a].sort()
# 1순위 : 먼저 풀어야 할 것 풀기 / 2순위 : 가능하면 쉬운 것 부터
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)
while heap:
    q = heapq.heappop(heap)
    print(q, end=' ')
    for i in arr[q]:
        indegree[i] -= 1
        if not indegree[i]:
            heapq.heappush(heap, i)