from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph):
    visited = [False] * (N + 1)
    visited[X] = True
    dq = deque([X])

    while dq:
        v = dq.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)

    return visited.count(True)


if __name__ == '__main__':
    N, M, X = map(int, input().split())
    in_order = [[] for _ in range(N + 1)]
    reversed_order = [[] for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, input().split())
        in_order[b].append(a)
        reversed_order[a].append(b)

    print(bfs(in_order), N - (bfs(reversed_order) - 1))


# img reference: http://dl.dropbox.com/s/wjr1sq7wwy5rk38/%EB%B0%B1%EC%A4%80-17616_%EB%93%B1%EC%88%98%20%EC%B0%BE%EA%B8%B0-2.png
