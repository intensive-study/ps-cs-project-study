def dfs(x, depth, dungeons):
    global answer, n
    if depth > answer:
        answer = depth
    for i in range(n):
        if x >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(x - dungeons[i][1], depth + 1, dungeons)
            visited[i] = False


def solution(k, dungeons):
    global answer, n, visited
    answer = 0
    n = len(dungeons)
    dungeons = sorted(dungeons, key=lambda x: -x[0])
    visited = [False] * n

    dfs(k, 0, dungeons)

    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

print(solution(k, dungeons))
