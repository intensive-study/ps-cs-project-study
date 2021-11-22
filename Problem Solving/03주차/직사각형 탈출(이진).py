import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

Sr, Sc, Fr, Fc = Sr-1, Sc-1, Fr-1, Fc-1 #(0,0)에 맞추기 위해서 1씩 빼줌.
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def checkWalls(board):
    walls = []
    for x in range(N):
        for y in range(M):
            if board[x][y] == 1:
                walls.append([x,y])
    return walls

walls = checkWalls(board)

def avoidWalls(nx, ny):
    if nx + H  > N or ny + W > M:
        return False

    if nx + H  <= N and ny + W <= M: # (0, 0) (0, 1) -> 0 + 2 - 1 = 1 # (0,4)가 가장 끝이므로 N보다 작은 값이어야함.
        for wx, wy in walls:
            if nx <= wx < nx + H and ny <= wy < ny + W: #직사각형안에 wall x, y가 있으면
                return False
    return True


def bfs():
    q = deque()
    q.append([Sr, Sc, 0])
    visited[Sr][Sc] = True

    while q:
        x, y, ans = q.popleft()
        if x == Fr and y == Fc:
            return ans

        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            # nx, ny 범위 안에 있고 벽을 잘 피한 상태이면
            if 0 <= nx < N and 0 <= ny < M:
                if avoidWalls(nx, ny) and not visited[nx][ny]: # 방문안했으면 방문표시
                    visited[nx][ny] = True
                    q.append([nx, ny, ans+1])
    return -1

print(bfs())