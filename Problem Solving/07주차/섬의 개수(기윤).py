import sys
from collections import deque

input = sys.stdin.readline

def isin(y, x, w, h):
    if -1<x<w and -1<y<h: return True
    return False

def bfs(sy, sx, w, h, visited, arr):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    d = ((0,1), (0,-1), (-1,0), (1,0), (1,1), (-1,1), (1,-1), (-1,-1))

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if not isin(ny, nx, w, h): continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if arr[ny][nx]: q.append((ny, nx))

if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if (w, h) == (0, 0): break
        arr = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False for _ in range(w)] for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if not visited[i][j] and arr[i][j]:
                    cnt += 1
                    bfs(i, j, w, h, visited, arr)
        
        print(cnt)