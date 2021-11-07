def solution(k, dungeons):
    global answer
    answer = 0
    # 정렬로 풀어보려했으나 실패
    # dungeons = sorted(dungeons, key = lambda x : (-x[0], x[1]))

    visited = [False] * len(dungeons)

    def dfs(x, depth):
        global answer
        answer = max(depth, answer) # depth는 통과한 던전 수
        for i in range(len(dungeons)):
            if x >= dungeons[i][0] and not visited[i]: # 피로도가 최소보다 크고 방문하지 않은 던전일 경우 재귀수행
                visited[i] = True
                dfs(x-dungeons[i][1], depth + 1)
                visited[i] = False

    dfs(k, 0)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))