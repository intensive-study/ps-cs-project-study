from collections import deque


def bfs(x, y, color):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dq = deque([(x, y)])
    visited[y][x] = True
    coordinate = deque([(x, y)])

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < X and 0 <= ny < Y:
                if graph[ny][nx] == color and not visited[ny][nx]:
                    dq.append([nx, ny])
                    coordinate.append((nx, ny))
                    visited[ny][nx] = True

    if len(coordinate) >= 4:
        while coordinate:
            idx_x, idx_y = coordinate.popleft()
            graph[idx_y][idx_x] = '.'
        return True
    else:
        return False


def drop():
    for i in range(X):
        idx = Y - 1
        for j in range(Y - 1, -1, -1):
            if graph[j][i] == '.':
                continue
            else:
                graph[idx][i], graph[j][i] = graph[j][i], graph[idx][i]
                idx -= 1


if __name__ == '__main__':
    cnt = 0
    X, Y = 6, 12
    graph = [list(input()) for _ in range(Y)]

    while True:
        visited = [[False] * X for _ in range(Y)]
        flag = False

        for i in range(Y):
            for j in range(X):
                if graph[i][j] != '.' and not visited[i][j]:
                    if bfs(j, i, graph[i][j]):
                        flag = True

        if flag:
            cnt += 1
        else:
            break
        # print(*graph, sep='\n')
        # print()
        drop()

    # print(*graph, sep='\n')
    print(cnt)

"""
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.

result = 3
"""
