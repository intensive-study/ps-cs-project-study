def dfs(node):
    removing_nodes.add(node)
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(i)


if __name__ == '__main__':
    N = int(input())
    graph = [set() for _ in range(N)]
    for i, v in enumerate(list(map(int, input().split()))):
        if v != -1:
            graph[v].add(i)
        else:
            continue
    removing_node = int(input())
    visited = [False] * N
    removing_nodes = set()

    dfs(removing_node)
    for i, v in enumerate(graph):
        graph[i] = v - removing_nodes

    cnt = 0
    for i, v in enumerate(graph):
        if i in removing_nodes:
            continue
        else:
            if not v:
                cnt += 1
    print(cnt)


"""
4
-1 0 0 1
3
"""