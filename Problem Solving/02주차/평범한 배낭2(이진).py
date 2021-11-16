import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N 물품수, M 무게
items = [map(int, input().split()) for _ in range(N)]  # V 무게 C 만족도 K 물건개수
dp = [0 for _ in range(M+1)]
w, s = [], []

for i in range(N):
    v, c, k = items[i]
    idx = 1
    temp = 0
    while k>0:
        temp = min(k, idx)
        w.append(v*temp)
        s.append(c*temp)

        idx *= 2
        k -= temp


for i in range(len(w)):
    for j in range(M, 0, -1):
        if j >= w[i]:
            dp[j] = max(dp[j] , dp[j-w[i]]+s[i])

print(dp[M])