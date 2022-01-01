import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
	dq = deque()

	for i in range(1, n+1):
		if indegree[i] == 0:
			dq.append(i)
			dp[i] = times[i]

	while dq:
		node = dq.popleft()
		for adj_node in graph[node]:
			indegree[adj_node] -= 1
			dp[adj_node] = max(dp[adj_node], dp[node]+times[adj_node])
			if indegree[adj_node] == 0:
				dq.append(adj_node)
	return dp



for _ in range(int(input())): #test case
	n, k = map(int, input().split()) # n : 건물 개수 / k : 규칙 개수
	times = [0]
	times.extend(list(map(int, input().split())))
	graph = [[] for _ in range(n+1)]
	indegree = [0] * (n+1)
	dp = [0] * (n+1)

	for _ in range(k):
		x, y = map(int, input().split())
		graph[x].append(y)
		indegree[y] += 1

	w = int(input()) # 건설할 건물 번호
	
	dp = topology_sort()
	print(dp[w])
