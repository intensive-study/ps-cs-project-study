import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        q = queue.popleft()
        for i in range(8):
            dx = nx[i] + q[0]
            dy = ny[i] + q[1]
            if dx < 0 or dx >= M or dy < 0 or dy >= N:
                continue
            if not arr[dx][dy] or visited[dx][dy]:
                continue
            visited[dx][dy] = 1
            queue.append((dx,dy))

while True:
    N, M = map(int, input().split())
    nx = [-1, -1, -1, 0, 1, 1, 1, 0]
    ny = [-1, 0, 1, 1, 1, 0, -1, -1]
    arr = []
    visited = [[0 for i in range(N)] for j in range(M)]
    ct = 0
    if N == 0 and M == 0:
        break
    for i in range(M):
        arr.append(list(map(int, input().split())))
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and arr[i][j] == 1:
                visited[i][j] = 1
                ct += 1
                BFS(i,j)
    print(ct)