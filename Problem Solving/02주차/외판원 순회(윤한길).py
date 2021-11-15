import sys
input = sys.stdin.readline
INF = float('inf')


def dfs(current, visited):
    if visited == (1 << n) - 1:  # 모든 도시를 방문했다면
        if graph[current][0]:  # 출발점으로 가는 경로가 있다면
            return graph[current][0]
        else:  # 출발점으로 가는 경로가 없다면
            return INF

    if dp[current][visited] != INF:  # 이미 최소비용이 계산되어 있다면
        return dp[current][visited]

    for i in range(1, n):  # 모든 도시를 탐방
        if not graph[current][i]:  # 가는 경로가 없다면
            continue
        if visited & (1 << i):  # 이미 방문한 도시라면
            continue

        dp[current][visited] = min(dp[current][visited], dfs(i, visited | (1 << i)) + graph[current][i])
        print(*dp, sep='\n')
        # print('---------------------------------------------------------------------------------')
    return dp[current][visited]


if __name__ == '__main__':
    n = int(input())
    dp = [[INF] * (1 << n) for _ in range(n)]
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    print(dfs(0, 1 << 0))

"""
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
result = 35
"""
