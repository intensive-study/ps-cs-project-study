'''
https://www.acmicpc.net/problem/1082
방 번호
골드4
'''

import sys
input = sys.stdin.readline

N = int(input())  # 3
P = list(map(int, input().split()))  # [6, 7, 8]
M = int(input())  # 21

dp = [-1 for _ in range(M+1)]
for i in range(N-1, -1, -1):
    start = P[i]
    for j in range(start, M+1):
        dp[j] = max(dp[j-start] * 10 + i, i, dp[j])
print(dp[M])