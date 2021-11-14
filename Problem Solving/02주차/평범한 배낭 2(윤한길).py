import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dp = [0] * (M + 1)
item_list_tmp = [list(map(int, input().split())) for _ in range(N)]
item_list = []

for i in item_list_tmp:
    cnt = i[2]
    idx = 1
    while cnt != 0:
        tmp = min(idx, cnt)
        item_list.append([i[0] * tmp, i[1] * tmp])
        cnt -= tmp
        idx *= 2
# print(item_list)

# 뒤에 부터 저장해서 tmp_dp를 만들 필요가없음
for v in item_list:
    for i in range(M, v[0] - 1, -1):
        dp[i] = max(dp[i], dp[i - v[0]] + v[1])

# print(dp)
print(dp[M])
"""
2 9
8 5 1
1 2 9
"""

"""
9 = 1+2+4+1+1
"""
