'''
Python3 1008ms
Pypy3 시간초과
우선순위 큐 사용
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