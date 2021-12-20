import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    arr = []
    MAX = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
    for i in range(1, N):
        for j in range(1, M):
            if arr[i][j] == 1:
                arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1
    print(max(map(max, arr)))