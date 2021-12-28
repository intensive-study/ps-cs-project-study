import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 0
answer = 0

while left < n:
    total = sum(arr[left:right+1])
    if total == m:
        answer += 1
        left = right
        right = left + 1
    
    elif total > m: left += 1
    else: right += 1

    if right == n:
        left += 1
        right = left

print(answer)