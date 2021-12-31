import sys
input = sys.stdin.readline

k, n = map(int, input().split())
cables_length = [int(input()) for _ in range(k)]

min_len, max_len = 1, max(cables_length)

while min_len <= max_len:
	mid_len = (min_len + max_len) // 2
	line_count = 0
	for cable_len in cables_length:
		line_count += cable_len // mid_len

	if line_count >= n:
		min_len = mid_len + 1
	else: # line_count < n
		max_len = mid_len - 1
print(max_len)