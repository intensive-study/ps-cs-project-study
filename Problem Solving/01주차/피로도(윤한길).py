from itertools import permutations


def solution(k, dungeons):
    possible_cases = []
    for per in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for i in per:
            if tmp >= i[0]:
                tmp -= i[1]
                cnt += 1
        possible_cases.append(cnt)

    return max(possible_cases)


def solution_with_backtracking(k, dungeons):
    global answer
    answer = 0
    n = len(dungeons)
    visited = [False] * n

    def dfs(k, dungeons, cnt):
        global answer
        if cnt > answer:
            answer = cnt

        for i in range(n):
            if dungeons[i][0] <= k and not visited[i]:
                visited[i] = True
                dfs(k - dungeons[i][1], dungeons, cnt+1)
                visited[i] = False

    dfs(k, dungeons, 0)

    return answer


if __name__ == '__main__':
    k, dungeons, result = 80, [[80, 20], [50, 40], [30, 10]], 3
    print(solution(k, dungeons))
    print(solution_with_backtracking(k, dungeons))
