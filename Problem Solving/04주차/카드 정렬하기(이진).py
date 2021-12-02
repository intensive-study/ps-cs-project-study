'''
Python3 1008ms
Pypy3 시간초과
우선순위 큐 사용
'''
'''
import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())

pq = PriorityQueue()
for _ in range(n):
    pq.put(int(input()))

total = 0
temp = 0

while pq.qsize() != 1:
    temp = pq.get() + pq.get()
    total += temp
    pq.put(temp)
print(total)    
'''


'''
heap 사용
Python3 216ms
'''
import sys
input = sys.stdin.readline
import heapq

n = int(input())
hq = []
for _ in range(n):
    heapq.heappush(hq, int(input()))
# hq.sort() 
# print(hq) 
total = 0
while len(hq) > 1:
    temp = heapq.heappop(hq) + heapq.heappop(hq)
    heapq.heappush(hq, temp)
    total += temp
print(total)