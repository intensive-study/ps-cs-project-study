import sys
input = sys.stdin.readline


def queen_cnt(l):
    cnt = 0
    for i in l:
        cnt += i.count(True)
    return cnt


def make_it_tuple(visited):
    l = []
    for i in visited:
        l.append(tuple(i))
    return tuple(l)


def get_diagonal_1(i, j):
    l = []
    for x in range(N):
        for y in range(N):
            if x - y == i - j:
                l.append(visited[x][y])
    return l


def get_diagonal_2(i, j):
    l = []
    for x in range(N):
        for y in range(N):
            if x + y == i + j:
                l.append(visited[x][y])
    return l


def dfs():
    global answer
    if queen_cnt(visited) == N:
        tmp = make_it_tuple(visited)
        if tmp not in check:
            check.add(tmp)
            answer += 1

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if True not in visited[i] and True not in list(zip(*visited))[j]:       # 가로, 세로 체크
                    if True not in get_diagonal_1(i, j) and True not in get_diagonal_2(i, j):
                        visited[i][j] = True
                        dfs()
                        visited[i][j] = False

    return


if __name__ == '__main__':
    global answer, check, N, visited
    check = set()
    answer = 0
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    dfs()

    print(answer)



"""
0 0   0 0 0
0 0   0 0 0
      0 0 0
"""