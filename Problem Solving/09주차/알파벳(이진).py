'''5688ms'''
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(r)]
alphabet = [0] * 26

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and alphabet[board[nx][ny]] == 0:
            alphabet[board[nx][ny]] = 1
            dfs(nx, ny, cnt+1)
            alphabet[board[nx][ny]] = 0


ans = 1
alphabet[board[0][0]] = 1
dfs(0, 0, ans)
print(ans)