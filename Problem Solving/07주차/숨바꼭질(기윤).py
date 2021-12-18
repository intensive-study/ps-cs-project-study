import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def bfs(n, adj):
    table = defaultdict(list)
    visited = [False for _ in range(n+1)]

    table[0].append(1)
    visited[1] = True
    q = deque()
    q.append((1, 0))
    
    while q:
        x, k = q.popleft()
        for nx in adj[x]:
            if visited[nx]: continue
            visited[nx] = True
            nk = k + 1
            table[nk].append(nx)
            q.append((nx, nk))
    
    return table

if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    table = bfs(n, adj)
    key = max(table.keys())
    print(min(table[key]), key, len(table[key]))