import sys
input = sys.stdin.readline
import heapq

n = int(input())
lst = []

for _ in range(n):
    day, cup = map(int, input().split())
    lst.append((day, cup))

lst.sort()

heap = []
for i in lst:
    heapq.heappush(heap,i[1])
    if i[0] < len(heap):
        heapq.heappop(heap)

print(sum(heap))