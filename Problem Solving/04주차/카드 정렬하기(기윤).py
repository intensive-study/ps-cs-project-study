from heapq import heappop, heappush, heapify
import sys

input = sys.stdin.readline
n = int(input())
bundles = [int(input()) for _ in range(n)]
heapify(bundles)
answer = 0

while bundles:
    if n == 1:
        if bundles[0] == 1: break
        answer = heappop(bundles)
    else:
        k = heappop(bundles) + heappop(bundles)
        answer += k
        if bundles: heappush(bundles, k)

print(answer)