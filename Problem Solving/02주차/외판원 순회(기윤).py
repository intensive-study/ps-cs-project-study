import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
INF = int(1e9)
dp = [[-1 for _ in range(1<<n)] for _ in range(n)]

def solve(node, visited):
    if visited == (1<<n) - 1:
        return arr[node][0] if arr[node][0] != 0 else INF

    if dp[node][visited] != -1: return dp[node][visited]

    cost = INF
    for x in range(n):
        if visited & (1<<x) == 0 and arr[node][x] != 0:
            cost = min(cost, solve(x, visited | (1<<x)) + arr[node][x])
    
    dp[node][visited] = cost
    return cost

print(solve(0, 1<<0))