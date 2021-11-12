from collections import deque

def bfs(x, adj):
    cnt = 0
    q = deque([x])
    visited[x] = True

    while q:
        v = q.popleft()
        for nv in adj[v]:
            if not visited[nv]:
                q.append(nv)
                visited[nv] = True
                cnt += 1
    return cnt

N, M, X = map(int, input().split())
upper = [[] for _ in range(N+1)] # b보다 점수가 큰 학생
lower = [[] for _ in range(N+1)] # a보다 점수가 작은 학생
visited = [False] * (N+1) #1부터 N까지의 학생

for _ in range(M):
    a, b = map(int, input().split())
    lower[a].append(b)
    upper[b].append(a)

#각 학생마다 upper rank 와 lower rank 리스트를 둬서 상대적인 순서 정보를 저장
#가능한 가장 높은 순위 : upper.size() + 1
#가능한 가장 낮은 순위 : N - lower.size()

print(bfs(X, upper) + 1, N - bfs(X, lower))