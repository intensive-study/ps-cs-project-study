from collections import deque
import sys
graph = []
queue = deque([])
m, n, h = map(int, sys.stdin.readline().split())
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tmp)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < h and  0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            queue.append([nx, ny, nz])
            graph[nx][ny][nz] = graph[x][y][z] + 1

day = 0
for h in graph:
    if any(0 in array for array in h):
        print(-1)
        exit(0)
    else:
        max_day =(max(map(max, h)))
        day = max(max_day, day)
print(day-1)
