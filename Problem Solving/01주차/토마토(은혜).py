from collections import deque

m, n, h = map(int, input().split())
box = [[] for _ in range(h)]
dir = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
q = deque([])
answer = -1

for i in range(h):
    for j in range(n):
        line = list(map(int, input().split()))
        box[i].append(line)
        for k in range(m):
            if line[k] == 1:
                q.append([i, j, k])

while q:
    x, y, z = q.popleft()
    for dx, dy, dz in dir:
        nx = x + dx
        ny = y + dy
        nz = z + dz
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
            if box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1 #다음날 익는 토마토에 기존 토마토 +1 날짜를 구현
                q.append([nx, ny, nz])

for l in box:
    for list in l:
        if 0 in list: # bfs 끝나고 안익은 토마토가 있을 경우
            print("-1")
            exit(0)
        else:
            answer = max(answer, max(list))

print(answer-1)

