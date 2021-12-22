import sys
input = sys.stdin.readline

while True:
	n = int(input())
	if n == 0: break

	profits = [int(input()) for _ in range(n)]
	for i in range(1, n):
		profits[i] = max(profits[i] + profits[i-1], profits[i])
	print(max(profits))