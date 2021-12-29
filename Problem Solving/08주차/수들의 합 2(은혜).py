import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum, r = 0, 0
cnt = 0

for l in range(N):
    while r < N and sum < M:
        sum += arr[r]
        r += 1
    if sum == M: 
        cnt += 1
    sum -= arr[l]
    
print(cnt)