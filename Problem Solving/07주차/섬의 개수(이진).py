import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

def dfs(graph, visited, x, y):
	visited[x][y] = True
	for i in range(8):
		nx, ny = x + dx[i], y + dy[i]

		if 0 <= nx < h and 0 <= ny < w:
			if not visited[nx][ny] and graph[nx][ny] == 1:
				dfs(graph, visited, nx, ny)


def bfs(graph, visited, x, y):
	q = deque([(x, y)])		
	while q:
		x, y = q.popleft()
		visited[x][y] = True
		for i in range(8):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == False:
				if graph[nx][ny] == 1:
					visited[nx][ny] = True
					q.append((nx, ny))


dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

while True:
	w, h = map(int, input().split())
	if w == 0 and h == 0: # 종료 조건
		break
	graph = [list(map(int, input().split())) for _ in range(h)]
	visited = [[False for _ in range(w)] for _ in range(h)]


	island = 0

	for i in range(h):
		for j in range(w):
			if not visited[i][j] and graph[i][j] == 1:
				# dfs(graph, visited, i, j)
				bfs(graph, visited, i, j)
				island += 1

	print(island)