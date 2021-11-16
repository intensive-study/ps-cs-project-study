import sys
input = sys.stdin.readline


def bfs(y, x):
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [input() for _ in range(N)]
    visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]
    iter_idx = iter([i for i in range(6)] * 2)
    d_idx = dict(a=next(iter_idx), b=next(iter_idx), c=next(iter_idx), d=next(iter_idx), e=next(iter_idx), f=next(iter_idx),
                 A=next(iter_idx), B=next(iter_idx), C=next(iter_idx), D=next(iter_idx), E=next(iter_idx), F=next(iter_idx))

    for i in range(N):
        for j in range(M):
            if graph[i][j] == '0':
                bfs(i, j)
