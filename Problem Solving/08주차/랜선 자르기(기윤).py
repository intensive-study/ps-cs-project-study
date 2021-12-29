import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

left = 1
right = max(arr)
answer = -1

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for num in arr: cnt += num // mid

    if cnt >= n:
        answer = max(answer, mid)
        left = mid + 1

    else: right = mid - 1

print(answer)