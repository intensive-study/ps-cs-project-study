N = int(input())
dp = [[0] * (1 << N) for _ in range(N)] # dp 행: 출발/도착도시 열: 방문한 도시 비트마스킹 표현, 값: 최단 거리
distance = [list(map(int, input().split())) for _ in range(N)] 
INF = float('inf') 

#순회할 수 있는 도시면 출발/도착지점 아무곳이나 선택가능, 0인 도시를 출발/도착 지점으로 설정

def dfs(current, visited):
    
    if visited == (1 << N) - 1 : # '1000000'-1 = 111111로 n개 모두 방문
        return distance[current][0] or INF  #모두 방문했을 경우 마지막 경로에서 도착지점으로 돌아올 수 있는 거리 반환

    if dp[current][visited]: # dp 값이 있으면 반환 없으면 넣어주는 과정 생략
        return dp[current][visited]

    tmp = INF
    for next in range(N): #다음 방문할 도시 확인
        if visited & (1 << next) == 0 and distance[current][next] != 0: # 방문하지 않았고 연결된 도시일 경우
            nowVisit  = visited | (1 << next) # 현재 방문한 도시 체크
            tmp = min(tmp, dfs(next, nowVisit) + distance[current][next])
    dp[current][visited] = tmp # visited 경로를 지나는 최단 거리
    
    print(dp)
    return tmp

print(dfs(0, 1 << 0)) 
