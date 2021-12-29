import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search(start, end):
    global ans
    while start <= end:
        mid = (start + end) // 2
        remain = 0
        for i in range(K):
            remain += arr[i] // mid
        if remain >= N:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

K, N = map(int, input().split())
ans = 0
arr = [int(input()) for i in range(K)]
binary_search(1, max(arr))
print(ans)