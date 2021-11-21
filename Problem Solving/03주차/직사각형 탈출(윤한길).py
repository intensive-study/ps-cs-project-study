from collections import deque
import sys
input = sys.stdin.readline


def bfs(start_y, start_x):
    visited[start_y][start_x] = True
    dq = deque([(start_y, start_x, 0)])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while dq:
        y, x, dist = dq.popleft()

        if y == F_r - 1 and x == F_c - 1:
            return dist

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    dq.append((ny, nx, dist + 1))


if __name__ == '__main__':
    N, M = map(int, input().split())
    visited = [list(map(int, input().split())) for _ in range(N)]
    H, W, S_r, S_c, F_r, F_c = map(int, input().split())

    # visited 만들기
    for i in range(N):
        for j in range(M):
            total = 0
            flag = False
            for k in range(H):
                if 0 <= i + H <= N and 0 <= j + W <= M:
                    total += sum(visited[i + k][j:j + W])
                else:
                    visited[i][j] = True
                    flag = True
            if not flag:
                visited[i][j] = False if total == 0 else True

    # print(*visited, sep='\n')
    print(bfs(S_r - 1, S_c - 1))
