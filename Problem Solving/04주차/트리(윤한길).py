def dfs(node):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(i)


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(N)]
    for i, v in enumerate(list(map(int, input().split()))):
        if v != -1:
            graph[i].append(v)
            graph[v].append(i)
        else:
            continue
    removing_node = int(input())
    print(graph)
    visited = [[False] * N]
    print(visited)
    dfs(0)
    print(visited)
