import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rsplit())
adj = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
q = deque()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rsplit())
    indegree[b] += 1
    adj[a].append(b)

for i in range(1, n+1):
    if not indegree[i]: q.append(i)

while q:
    node = q.popleft()
    print(node, end=' ')

    for neighbor in adj[node]:
        indegree[neighbor] -= 1
        if not indegree[neighbor]: q.append(neighbor)