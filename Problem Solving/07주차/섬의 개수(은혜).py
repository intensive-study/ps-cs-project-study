from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(y, x):
    visited[y][x] = True
    dir = [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1),(1,-1),(-1,1)]
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < w and ny >= 0 and ny < h and field[ny][nx] == '1' and not visited[ny][nx]:
            dfs(ny, nx)
            
while True:
    w, h = map(int, input().split())
    
    if w == 0: #테스트케이스 끝나면 종료
        break

    field = []
    visited = [[False] * w for _ in range(h)]
    
    for _ in range(h):
        field.append(input().split())
        
    count = 0
    for i in range(w): #x범위
        for j in range(h): #y범위
            if field[j][i] == '1' and not visited[j][i]:
                dfs(j, i)
                count += 1
    print(count)