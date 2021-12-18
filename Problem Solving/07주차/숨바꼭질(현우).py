import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(x):
    queue = deque()
    queue.append((x,0))
    while queue:
        q = queue.popleft()
        for i in arr[q[0]]:
            if visited[i] == -1:
                visited[i] = q[1]+1
                queue.append((i, q[1]+1))

N, M = map(int, input().split())
arr = [[] for i in range(20001)]
visited = [-1] * (20001)
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(N+1):
    arr[i].sort()
visited[1] = 0
BFS(1)
ans = max(visited)
print(visited.index(ans), ans, visited.count(ans))