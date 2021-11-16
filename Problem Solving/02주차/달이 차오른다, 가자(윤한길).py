from collections import deque
import sys
input = sys.stdin.readline


def bfs(y, x, init_keys):
    visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]
    iter_idx = iter([i for i in range(6)] * 2)
    d_key = dict(a=next(iter_idx), b=next(iter_idx), c=next(iter_idx), d=next(iter_idx), e=next(iter_idx), f=next(iter_idx))
    d_door = dict(A=next(iter_idx), B=next(iter_idx), C=next(iter_idx), D=next(iter_idx), E=next(iter_idx), F=next(iter_idx))
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    dq = deque([(y, x, init_keys, 0)])
    visited[y][x][init_keys]

    while dq:
        y, x, keys_status, cnt = dq.popleft()
        if graph[y][x] == '1':
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] != '#' and not visited[ny][nx][keys_status]:
                    if graph[ny][nx] in ['.', '1', '0']:
                        dq.append((ny, nx, keys_status, cnt + 1))
                        visited[ny][nx][keys_status] = True
                    elif graph[ny][nx] in d_key:
                        tmp = keys_status | (1 << d_key[graph[ny][nx]])
                        dq.append((ny, nx, tmp, cnt + 1))
                        visited[ny][nx][tmp] = True
                    elif graph[ny][nx] in d_door:
                        if keys_status & (1 << d_door[graph[ny][nx]]):
                            dq.append((ny, nx, keys_status, cnt + 1))
                            visited[ny][nx][keys_status] = True


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [input() for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '0':
                coordinate = (i, j)
                flag = True
                break
        if flag:
            break

    answer = bfs(coordinate[0], coordinate[1], 0 << 0)
    if answer:
        print(answer)
    else:
        print(-1)
