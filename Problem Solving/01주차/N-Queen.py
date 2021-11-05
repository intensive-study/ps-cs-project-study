# import sys
# input = sys.stdin.readline
#
#
# def queen_cnt(l):
#     cnt = 0
#     for i in l:
#         cnt += i.count(True)
#     return cnt
#
#
# def make_it_tuple(visited):
#     l = []
#     for i in visited:
#         l.append(tuple(i))
#     return tuple(l)
#
#
# def get_diagonal_1(i, j):
#     l = []
#     for x in range(N):
#         for y in range(N):
#             if x - y == i - j:
#                 l.append(visited[x][y])
#     return l
#
#
# def get_diagonal_2(i, j):
#     l = []
#     for x in range(N):
#         for y in range(N):
#             if x + y == i + j:
#                 l.append(visited[x][y])
#     return l
#
#
# def dfs():
#     global answer
#     if queen_cnt(visited) == N:
#         tmp = make_it_tuple(visited)
#         if tmp not in check:
#             check.add(tmp)
#             answer += 1
#
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 if True not in visited[i] and True not in list(zip(*visited))[j]:       # 가로, 세로 체크
#                     if True not in get_diagonal_1(i, j) and True not in get_diagonal_2(i, j):
#                         visited[i][j] = True
#                         dfs()
#                         visited[i][j] = False
#
#     return
#
#
# if __name__ == '__main__':
#     global answer, check, N, visited
#     check = set()
#     answer = 0
#     N = int(input())
#     visited = [[False] * N for _ in range(N)]
#     dfs()
#
#     print(answer)

# 행(row)로 접근하고, (row + 1)로 재귀적으로 진입해서 중첩처리 제거 & 가로 공격 범위 조건 체크 제거
def dfs(row):
    global answer

    if row == n:
        answer += 1

    for col in range(n):
        # 대각선, 세로만 체크 중 하나라도 set에 있으면 퀸공격 가능범위이므로 continue
        if col in colSet or (row + col) in posDiag or (row - col) in negDiag:
            continue

        # 퀸공격 범위에 없으면 각 set에 값 넣기
        colSet.add(col)
        posDiag.add(row + col)
        negDiag.add(row - col)

        # 같은 행에 퀸이 존재할수 없으므로 row + 1로 재귀진입 -> 가로조건 자동 체크해줌 + 백트래킹 시 중첩처리 막아줌
        dfs(row + 1)

        # 백트래킹
        colSet.remove(col)
        posDiag.remove(row + col)
        negDiag.remove(row - col)


if __name__ == '__main__':
    global answer
    n = int(input())
    answer = 0

    colSet = set()   # (col)
    posDiag = set()  # (row + col)
    negDiag = set()  # (row - col)

    dfs(0)
    print(answer)

"""
0 1   0 1 2   0 1 2 3
2 3   3 4 5   4 5 6 7
      6 7 8   8 9 10 11
              12 13 14 15
"""
