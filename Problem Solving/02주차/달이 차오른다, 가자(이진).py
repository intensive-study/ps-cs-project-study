import sys
from collections import deque
input = sys.stdin.readline

# dx : 행, dy : 열
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 시작하는 위치 x, y
def bfs(x, y):
    # 시작하는 위치를 q에 넣어주고 방문표시해줌
    q.append([x,y,0])
    visited[x][y][0] = 1
    
    while q:
        x, y, key = q.popleft()
        # 1인 경우 끝냄.
        if board[x][y] == '1':
            print(visited[x][y][key] - 1)
            return
        
        # 1이 아닌 경우
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # board 범위 안에 있을때
            if 0 <= nx < N and 0 <= ny < M:
                # '#'(벽)이 아니고, 방문한적 없는 위치일때
                if board[nx][ny] != '#' and visited[nx][ny][key] == 0:
                    # 그 위치가 소문자이면 -> 키가 있는거임.
                    if board[nx][ny].islower():
                        # key에 새로운 키값 더하기
                        nkey = key | (1<<(ord(board[nx][ny]) - ord('a'))) # ord('a') = 97
                        # 방문 안했으면
                        if visited[nx][ny][nkey] == 0:
                            visited[nx][ny][nkey] = visited[x][y][key] + 1
                            q.append([nx, ny, nkey])
                    # 그 위치가 대문자이면 -> 문이 있는거임.
                    elif board[nx][ny].isupper():
                        # key랑 겹치는 문이 있으면 방문하고 q에 넣어줌.
                        if key & (1<<(ord(board[nx][ny]) - ord('A'))): # ord('a') = 97
                            visited[nx][ny][key] = visited[x][y][key] + 1
                            q.append([nx, ny, key])
                    # 
                    else:
                        visited[nx][ny][key] =visited[x][y][key] + 1
                        q.append([nx, ny, key])
                        
    # 갈수 없을 경우 -1을 프린트한다.
    print(-1)
                        
# N : 세로 M : 가로
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
ALL_KEYS = 1 << 6  # KEYS = 'f', 'e', 'd', 'c', 'b', 'a'
visited = [[[0]*ALL_KEYS for _ in range(M)] for _ in range(N)]            
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            # 시작하는 위치 i, j
            bfs(i, j)