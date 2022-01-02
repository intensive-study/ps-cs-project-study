import sys

input = sys.stdin.readline
R, C = map(int, input().split())
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [input().strip() for _ in range(R)]
trace = [(0, 0, board[0][0])]
answer = 1
    
while trace:
    x, y, strs = trace.pop()
    
    for (dx, dy) in dir:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < R and 0 <= ny < C and (board[nx][ny] not in strs):
            trace.append((nx, ny, strs + board[nx][ny]))
            answer = max(answer, len(strs) + 1)
            
print(answer)