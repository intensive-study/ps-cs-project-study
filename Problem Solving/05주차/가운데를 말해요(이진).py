import sys
import heapq

input = sys.stdin.readline
n = int(input())
leftHeap, rightHeap = [], []
for i in range(n):
	num = int(input())
	# if i == 0:#first
	# 	heapq.heappush(leftHeap, -num)

	if len(leftHeap) == len(rightHeap):
		heapq.heappush(leftHeap, -num)
	else:
		heapq.heappush(rightHeap, num)

	if leftHeap and rightHeap and (-leftHeap[0]) > rightHeap[0]:
		left = -heapq.heappop(leftHeap)
		right = heapq.heappop(rightHeap)
		heapq.heappush(rightHeap, left)
		heapq.heappush(leftHeap, -right)
	print(-leftHeap[0])	