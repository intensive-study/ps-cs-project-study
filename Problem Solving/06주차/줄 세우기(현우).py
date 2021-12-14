import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ct = [0] * (N+1)
arr = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    ct[b] += 1

#ct가 0인 것을 먼저 집어넣음
queue = deque()
for i in range(1, N+1):
    if not ct[i]:
        queue.append(i)
while queue:
    q = queue.popleft()
    print(q, end= ' ')
    for i in arr[q]:
        ct[i] -= 1
        if not ct[i]:
            queue.append(i)