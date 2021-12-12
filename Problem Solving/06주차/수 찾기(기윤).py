import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
nums = tuple(map(int, input().split()))

for num in nums:
    left = 0
    right = n-1
    ok = False
    while left <= right:
        mid = (left+right) // 2
        if A[mid] == num:
            ok = True
            break

        elif A[mid] < num: left = mid + 1
        elif A[mid] > num: right = mid - 1
    
    print(int(ok))