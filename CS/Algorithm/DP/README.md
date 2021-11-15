# Longest Increasing Subsequence

    import sys
    from bisect import bisect_left
    
    input = sys.stdin.readline
    
    
    def LIS_with_dp():  # O(n^2)
        x = int(input())
        arr = list(map(int, input().split()))
        dp = [1 for i in range(x)]
    
        for i in range(x):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
    
        print(max(dp))
    
    
    def LIS_with_dp_and_bisect():  # O(nlog(n))
        N = int(input())
        input_list = list(map(int, input().split()))
    
        # dp input_list[0]로 초기화
        dp = [input_list[0]]
    
        for i in range(N):
            # 현재 순회중인 원소가 dp에 제일 마지막에 들어간 값보다 크면 dp에 값을 추가해주기
            if input_list[i] > dp[-1]:
                dp.append(input_list[i])
            # 현재 순회중인 원소가 dp의 마지막 값보다 작을시, 그 값을 dp에서 이분탐색하여 들어갈수 있는 위치에 넣기
            else:
                idx = bisect_left(dp, input_list[i])
                dp[idx] = input_list[i]
    
        print(len(dp))
    
    
    if __name__ == '__main__':
        LIS_with_dp()
        LIS_with_dp_and_bisect()
    
    '''
    6
    10 20 12 30 20 50
    '''

# Lowest Common Ancestor
- [참고자료](https://velog.io/@shiningcastle/%EC%B5%9C%EC%86%8C-%EA%B3%B5%ED%86%B5-%EC%A1%B0%EC%83%81-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

# Dynamic Programming
복잡한 문제를 간단한 여러개의 하위 문제로 나누어 푸는 방법
  - Top-down : 가장 큰 문제를 방문 후 작은 문제를 재귀적으로 호출하여 답을 찾는 방식
    - 장점 : 점화식을 이해하기 쉽다
    

            d = [0 for _ in range(100)]
            
            
            def fibo(x):
                if x == 1 or x == 2:
                    return 1
                if d[x] != 0:
                    return d[x]
                else:
                    d[x] = fibo(x - 1) + fibo(x - 2)
                return d[x]
            
            
            print(fibo(99))


  - Bottom-up : 가장 작은 문제로 시작해서 전체 문제의 답을 찾는 방식
    - 장점 : 함수를 재귀적 호출하지 않아도 되기에 시간, 메모리 사용량을 줄일수 있다
    

            dp = [0 for i in range(100)]
            dp[1], dp[2] = 1, 1
            
            
            def fibo(x):
                for i in range(3, x + 1):
                    dp[i] = dp[i - 1] + dp[i - 2]
                return dp[x]
            
            
            print(fibo(99))


# 다익스트라

    #개선된 다익스트라 알고리즘
    
    import heapq
    import sys
    
    input = sys.stdin.readline
    INF = int(1e9)
    
    #노드 갯수, 간선 갯수
    n, m = map(int, input().split())
    
    #시작 노드
    start = int(input())
    
    #각 노드에 연결되어 있는 노드정보 저장할 곳
    graph = [[] for i in range(n+1)]
    
    #최단거리 테이블 초기화
    distance = [INF] * (n+1)
    
    #간선 정보 입력받기
    for _ in range(m):
      a, b, c = map(int, input().split())
      graph[a].append((b, c))
    
    def dijkstra(start):
      q = []
      #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
      heapq.heappush(q, (0, start))
      distance[start] = 0
    
      while q:  #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
          continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
          cost = dist + i[1]
          #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
          if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
    
    dijkstra(start)
    
    for i in range(1, n+1):
      if distance[i] == INF:
        print("INFINITY")
      else:
        print(distance[i])

# 비트마스크
- [참고](https://justkode.kr/algorithm/bitmash)