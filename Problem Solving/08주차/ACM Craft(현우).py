import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def topological_sort():
    queue = deque()
    for i in range(N):
        if not indegree[i]:
            queue.append(i)
            dp[i] = time[i]
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            dp[i] = max(dp[q] + time[i], dp[i])
            indegree[i] -= 1
            if not indegree[i]:
                queue.append(i)

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    indegree = [0] * (N+1)
    graph = [[] for i in range(N)]
    dp = [0] * N
    time = list(map(int, input().split()))
    for j in range(K):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        indegree[b-1] += 1
    W = int(input())
    topological_sort()
    print(dp[W-1])