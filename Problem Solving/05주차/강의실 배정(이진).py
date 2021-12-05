# 384ms
import heapq
import sys

input = sys.stdin.readline
 
N = int(input())
arr = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    arr.append([A, B])
 
arr.sort(key=lambda x: x[0])
time = []
heapq.heappush(time, arr[0][1])
for i in range(1, N):
	if time[0] > arr[i][0]:
		heapq.heappush(time, arr[i][1])
	else:
		heapq.heappop(time)
		heapq.heappush(time, arr[i][1])
print(len(time))