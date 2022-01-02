import sys
import heapq
input = sys.stdin.readline

tc = int(input())
arr = []
hq = []

for _ in range(tc):
    dd, rm = map(int, input().split())
    arr.append((dd, rm))
    
arr.sort(key = lambda x : -x[0])

time = 0
while arr:
    (dd, rm) = arr.pop()
    if dd > time:
        heapq.heappush(hq, rm)
        time += 1
    elif hq: #데드라인이 이전과 크거나 같기 때문에, 하나 제거하고 추가 가능
        own = hq[0]
        if rm > own:
            heapq.heappop(hq)
            heapq.heappush(hq, rm)
            
print(sum(hq))

# 예외 케이스 참고 https://velog.io/@ju_h2/Python-%EB%B0%B1%EC%A4%80-1781.-%EC%BB%B5%EB%9D%BC%EB%A9%B4-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B5%AC%ED%98%84-6
    
