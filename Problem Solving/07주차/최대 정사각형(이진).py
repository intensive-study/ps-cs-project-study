import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    squares = [list(map(int, input().split())) for _ in range(n)]


    max_len = 0

    for i in range(1, n):
        for j in range(1, m):
            if squares[i][j] == 1:
                squares[i][j] += min(squares[i-1][j], squares[i][j-1], squares[i-1][j-1])

    print(max(map(max, squares)))


'''
while True:
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		break
	squares = [list(map(int, input().split())) for _ in range(n)]
	dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

	max_len = 0

	for i in range(n):
		for j in range(m):
			if squares[i][j] == 1:
				dp[i+1][j+1] += min(dp[i+1][j], dp[i][j+1], dp[i][j])+1
		row_max = max(dp[i+1])
		max_len = max(row_max, max_len)

	print(max_len)
'''