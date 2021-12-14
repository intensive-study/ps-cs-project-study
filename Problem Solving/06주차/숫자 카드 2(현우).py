import sys
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr.sort()
for i in arr2:
    print(bisect_right(arr, i) - bisect_left(arr, i), end=' ')