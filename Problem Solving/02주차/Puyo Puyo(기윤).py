import sys
from collections import deque

r, c = 12, 6
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
q = deque()

def isin(y, x):
    if -1<y<r and -1<x<c: return True
    return False

def bfs(sy, sx):
    d = ((1,0), (-1,0), (0,1), (0,-1))
    q.append((sy, sx))
    visited[sy][sx] = True
    items = [(sy, sx)]

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if not isin(ny, nx): continue
            if not visited[ny][nx] and arr[ny][nx] == arr[sy][sx]:
                visited[ny][nx] = True
                q.append((ny, nx))
                items.append((ny, nx))
    
    return items
                
def remove(items):
    if len(items) < 4: return False
    for y, x in items: arr[y][x] = '.'
    return True

def down():
    for x in range(c):
        for y in range(r-2, -1, -1):
            _y = y + 1
            while _y < r:
                if arr[_y][x] != '.': break
                _y += 1
            
            if _y-1 == y: continue
            arr[_y-1][x] = arr[y][x]
            arr[y][x] = '.'

ok = True
answer = 0
while ok:
    ok = False
    visited = [[False for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and arr[i][j] != '.':
                items = bfs(i,j)
                if remove(items): ok = True
                 
    if ok: 
        down()
        answer += 1

print(answer)