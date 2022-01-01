import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []
arr = [list(map(int, input().split())) for i in range(N)]
arr.sort()

for i in range(N):
    heapq.heappush(heap, arr[i][1])
    if arr[i][0] < len(heap):
        heapq.heappop(heap)
print(sum(heap))