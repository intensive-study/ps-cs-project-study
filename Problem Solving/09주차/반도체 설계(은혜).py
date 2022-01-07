import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n) :
    for j in range(0, i) :
        if arr[i] > arr[j] : 
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))