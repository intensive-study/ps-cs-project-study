import sys
from collections import deque

def bfs(X, lst):
    cnt = 0
    queue = deque()
    queue.append(X)
    visited[X] = True

    while queue:
        v = queue.popleft()
        for nv in lst[v]:
            if not visited[nv]:
                queue.append(nv)
                visited[nv] = True
                cnt += 1
    return cnt

N, M, X = map(int, sys.stdin.readline().split())
high = [[] for _ in range(N+1)]
low = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    high[a].append(b)
    low[b].append(a)

print(1+bfs(X, low), N-bfs(X, high))