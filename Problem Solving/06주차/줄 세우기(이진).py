# 252ms

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree_list = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree_list[b] += 1

def topology_sort():
    answer = []
    q = deque()

    for i in range(1, n+1):
        if indegree_list[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        answer.append(node)
        for i in graph[node]:
            indegree_list[i] -= 1
            if indegree_list[i] == 0:
                q.append(i)
    return answer

answer = topology_sort()
print(*answer)