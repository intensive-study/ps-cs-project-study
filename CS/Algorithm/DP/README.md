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
