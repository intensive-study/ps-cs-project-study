#시간초과
'''
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

numSets = []
dp = [0 for i in range(n+1)]

for i in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0: # 합집합
        if a == b:
            continue
        
        if dp[a] == 0 and dp[b] == 0:
            dp[a] += i+1
            dp[b] += i+1
        else:
            temp = min(dp[a], dp[b])
            dp[a], dp[b] = max(dp[a], dp[b]), max(dp[a], dp[b])
            for j in range(n+1):
                if dp[j] == temp:
                    dp[j] = max(dp[a], dp[b])

    if op == 1: # check
        if dp[a] == dp[b]:
            print('YES')
        else:
            print("NO")
'''

# Union-Find
# 110088kb	604ms
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = [i for i in range(n+1)]

def find(x):
	if x == lst[x]:
		return x
	lst[x] = find(lst[x])
	return lst[x]

def union(a, b):
	a = find(a)
	b = find(b)

	if a < b:
		lst[b] = a
	else:
		lst[a] = b


for i in range(m):
	op, a, b = map(int, input().split())

	if op == 0:
		union(a, b)

	else:
		if find(a) == find(b): print("YES")
		else: print("NO")