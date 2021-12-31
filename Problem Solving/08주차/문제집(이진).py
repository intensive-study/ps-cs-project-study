# from collections import deque
import heapq

def topology_sort():
    answer = []
    dq = []

    for i in range(1, n+1):
        if indegree_list[i] == 0:
            heapq.heappush(dq, i)
            # dq.append(i)

    while dq:
        node = heapq.heappop(dq)
        # node = dq.popleft()
        answer.append(node)
        for i in graph[node]:
            indegree_list[i] -= 1
            if indegree_list[i] == 0:
                heapq.heappush(dq, i)
                # dq.append(i)
    return answer


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree_list = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree_list[b] += 1

answer = topology_sort()
print(*answer)