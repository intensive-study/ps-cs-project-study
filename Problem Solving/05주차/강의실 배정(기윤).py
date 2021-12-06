import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort()
rooms = []
heappush(rooms, lectures[0][1])
for i in range(1, n):
    if lectures[i][0] >= rooms[0]: heappop(rooms)
    heappush(rooms, lectures[i][1])

print(len(rooms))