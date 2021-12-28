import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
total = 0
ans = 0
for start in range(N):
    while total < M and end < N:
        total += arr[end]
        end += 1
    if total == M:
        ans += 1
    total -= arr[start]
print(ans)