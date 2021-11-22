from collections import deque


def bfs(y, x, init_keys):
    visited = [[[False] * (1 << 2) for _ in range(M)] for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dq = deque([(y, x, init_keys, (0, 0), 0)])

    while dq:
        y, x, keys_status, curr_dir, cnt = dq.popleft()

        if graph[y][x] == 'C' and keys_status == ((1 << 2) - (1 << 0)):
            return cnt
        # (1, 1, 1, (0, 1), 2), (1, 1, 1, (0, -1), 2)
        # (0, 1, 1, (-1, 0), 3), (2, 1, 1, (1, 0), 3),
        # (1, 1, 1, (-1, 0), 4), (1, 1, 1, (-1, 0), 4)
        for direction in directions:
            if curr_dir == direction:
                continue
            ny = y + direction[0]
            nx = x + direction[1]

            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] != '#' and not visited[ny][nx][keys_status]:
                    if graph[ny][nx] == '.':
                        dq.append((ny, nx, keys_status, direction, cnt + 1))
                        visited[ny][nx][keys_status] = True
                    elif graph[ny][nx] == 'S':
                        dq.append((ny, nx, keys_status, direction, cnt + 1))
                    elif graph[ny][nx] == 'C':
                        if keys_status == (0 << 0):
                            tmp = keys_status | (1 << 0)
                            dq.append((ny, nx, tmp, direction, cnt + 1))
                            visited[ny][nx][tmp] = True
                        elif keys_status == (1 << 0):
                            tmp = keys_status | (1 << 1)
                            dq.append((ny, nx, tmp, direction, cnt + 1))
                            visited[ny][nx][tmp] = True
    return -1


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'S':
                print(bfs(i, j, 0 << 0))
