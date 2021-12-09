'''
https://www.acmicpc.net/problem/1450
냅색문제
골드1
'''

# 184ms

import sys
input = sys.stdin.readline

n, c = map(int, input().split())  # n = 4, c = 6
weights = list(map(int, input().split()))  # 1, 5, 3, 2
weights_a = weights[:ceil(n/2)]  # 1, 5
weights_b = weights[ceil(n/2):]  # 3, 2

subset_sum_a, subset_sum_b = [], []

def sum_of_subsets(start, end, weight_arr, sumarr_subsets):
	if start >= len(weight_arr):
		sumarr_subsets.append(end)
		return
	sum_of_subsets(start + 1, end, weight_arr, sumarr_subsets)
	sum_of_subsets(start + 1, end + weight_arr[start], weight_arr, sumarr_subsets)


def binary_search(start, end, arr, target):
	while start < end:
		mid = (start + end) // 2
		if arr[mid] <= target:
			start = mid + 1
		else:
			end = mid
	return end


sum_of_subsets(0, 0, weights_a, subset_sum_a)
sum_of_subsets(0, 0, weights_b, subset_sum_b)
subset_sum_b.sort() ##### 필수!!
# print(subset_sum_a)
# print(subset_sum_b)

ans = 0
for a in subset_sum_a:
	if c - a >= 0:
		ans += binary_search(0, len(subset_sum_b), subset_sum_b, c-a)

print(ans)