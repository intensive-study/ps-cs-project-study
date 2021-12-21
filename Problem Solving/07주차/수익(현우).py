import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    N = int(input())
    if not N:
        break
    arr = []
    for i in range(N):
        arr.append(int(input()))
    for i in range(1, len(arr)):
        arr[i] = max(arr[i-1]+arr[i], arr[i])
    print(max(arr))