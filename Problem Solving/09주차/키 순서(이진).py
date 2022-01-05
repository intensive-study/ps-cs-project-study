import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1
cnt = 0
for i in range(n):
    t = 0
    for j in range(n):
        t += graph[i][j] + graph[j][i]
    if t == n-1:
        cnt += 1
print(cnt)