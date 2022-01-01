import sys
from collections import deque

input = sys.stdin.readline
tc = int(input())

while tc:
    n, k = map(int, input().split())
    indegree = [0] * (n+1)
    adj = [[] for _ in range(n+1)]
    time = [-1] + list(map(int, input().split()))
    q = deque()
    result = [-1] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        adj[a].append(b)
        indegree[b] += 1
    
    w = int(input())

    for i in range(1, n+1):
        if not indegree[i]: 
            result[i] = time[i]
            q.append(i)

    for i in range(1, n+1):
        if not q: break
        x = q.popleft()
        for nx in adj[x]:
            result[nx] = max(result[x]+ time[nx], result[nx])
            indegree[nx] -= 1
            if not indegree[nx]: q.append(nx)

    print(result[w])
    tc -= 1