import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ct = 0
arr = [list(input()) for i in range(N)]
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if arr[i][j] == '1':
            ct += 1
            for x in range(i+1):
                for y in range(j+1):
                    if arr[x][y] == '0':
                        arr[x][y] = '1'
                    else:
                        arr[x][y] = '0'
print(ct)