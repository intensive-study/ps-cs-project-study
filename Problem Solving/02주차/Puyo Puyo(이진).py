import sys
from collections import deque
input = sys.stdin.readline

# dx : 행, dy : 열
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    colors = set() # 존재하는 색을 저장하는 변수
    
    while q:
        qx, qy = q.popleft()
        # colors에 이미 저장되어있었다면 continue
        if (qx, qy) in colors:
            continue
        colors.add((qx, qy))
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            # 범위안에 존재하고
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                # 현재 색과 이동하는 위치nx,ny의 색이 같으면 q에 넣어줌
                if board[qx][qy] == board[nx][ny]:
                    q.append((nx, ny))
    return colors

# 아래가 비어있을때 떨어뜨리는 함수
def falling():
    # 열마다 살피고
    for c in range(COLS):
        # 행마다 아래부터 살필때
        for r in range(ROWS-1, -1, -1):
            # .이 아닐 경우
            if board[r][c] != '.':
                for k in range(ROWS-1, r, -1):
                    if board[k][c] == '.':
                        board[k][c] = board[r][c]
                        board[r][c] = '.'


ROWS = 12
COLS = 6

board = [list(input().strip()) for _ in range(ROWS)]
count = 0 # 몇연쇄 터지는지

while True:
    check = 0
    # board를 가장 아래부터 살펴봐야하므로
    for i in range(ROWS-1, -1, -1):
        for j in range(COLS):
            if board[i][j] == '.':
                continue
            colors = bfs(i, j)
            if len(colors) >= 4:
                if check == 0:
                    check = 1
                for x, y in colors:
                    board[x][y] = '.'
    falling()
    if check == 1:
        count += 1
    else:
        break
print(count)