import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS(x, y, st):
    global MAX
    MAX = max(MAX, len(st))
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if dx < 0 or dx >= R or dy < 0 or dy >= C:
            continue
        if visited[dx][dy] == 1:
            continue
        if arr[dx][dy] not in st:
            visited[dx][dy] = 1
            DFS(dx, dy, st+arr[dx][dy])
            visited[dx][dy] = 0

R, C = map(int, input().split())
MAX = -1
nx = [-1, 0, 1, 0]
ny = [0, -1, 0 ,1]
arr = [input() for i in range(R)]
visited = [[0 for i in range(C)] for j in range(R)]
visited[0][0] = 1
DFS(0, 0, arr[0][0])
print(MAX)