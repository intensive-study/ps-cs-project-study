import sys
input = sys.stdin.readline

def solution(last, visited):
    # 모두 방문했으면
    if visited == VISITED_ALL:
        # 끝지점에서 시작점까지 경로가 있다면 graph[last][0], 없으면 INF 리턴
        return W[last][0] or INF
    # 이미 계산되어있으면 있는 값 반환
    if dp[last][visited] is not None:
        return dp[last][visited]

    tmp = INF
    for city in range(N):
        # 아직 방문 안한 도시 and 길이 있을 경우
        if visited & (1 << city) == 0 and W[last][city] != 0:
            # tmp를 tmp와 다른 도시들까지 최소 거리
            # + 지금 도시에서 다른 도시까지 거리 중 작은 값으로 갱신한다.
            tmp = min(tmp,
                      solution(city, visited | (1 << city)) + W[last][city])
    dp[last][visited] = tmp
    return tmp


N = int(input())  # 도시의 수
W = [list(map(int, input().split())) for _ in range(N)]  #비용
dp = [[None] * (1 << N) for _ in range(N)]

# ans변수를 무한으로 초기화, 경로 찾을때마다 더 작은값으로 경신해 최종값 구함.
INF = float('inf')
ans = INF
# 모든 도시 방문했음을 의미하는 상수
VISITED_ALL = (1 << N) - 1

answer = solution(0, 1<<0)
print(answer)