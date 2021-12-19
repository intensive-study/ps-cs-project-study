import sys
input = sys.stdin.readline
from collections import deque


def bfs(node):
	q = deque([node])
	visited[node] = 1
	while q:
		pop_node = q.popleft()
		for node in graph[pop_node]:
			if visited[node] == 0:
				visited[node] = visited[pop_node] + 1
				q.append(node)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	a_i, b_i = map(int, input().split())
	graph[a_i].append(b_i)
	graph[b_i].append(a_i)

visited = [0] * (n+1)
bfs(1)

max_idx = visited.index(max(visited))
max_distance = max(visited) - 1
same_distance = visited.count(max(visited))

print(max_idx, max_distance, same_distance)