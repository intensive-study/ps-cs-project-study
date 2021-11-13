import sys

input = sys.stdin.readline
N, K = map(int, input().split())
item_list = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

# Bottom Up
# tmp_dp = [0] * (K+1)
# for v in item_list:
#     for i in range(1, K+1):
#         if i >= v[0]:
#             dp[i] = max(tmp_dp[i], tmp_dp[i-v[0]] + v[1])
#     tmp_dp = dp[:]  # shallow copy

# Top Down
# 뒤에 부터 저장해서 tmp_dp를 만들 필요가없음
for v in item_list:
    for i in range(K, v[0] - 1, -1):
        dp[i] = max(dp[i], dp[i - v[0]] + v[1])

# print(dp)
print(dp[K])
