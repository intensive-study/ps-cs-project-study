import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
prime = []
arr = [1] * (N+1)
arr[0] = 0
arr[1] = 0
for i in range(2, N+1):
    if arr[i] == 1:
        prime.append(i)
        for j in range(i+i, N+1, i):
            if arr[j] == 1:
                arr[j] = 0

#이제부터 투 포인터
ans = 0
start, end = 0, 0
total = 0
for start in range(len(prime)):
    while total < N and end < len(prime):
        total += prime[end]
        end += 1
    if total == N:
        ans += 1
    total -= prime[start]
print(ans)