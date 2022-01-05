import sys

def input():
    return sys.stdin.readline().rstrip()

def union(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

N = int(input())
M = int(input())
total = 0
parent = [i for i in range(N+1)]
arr = [list(map(int, input().split())) for i in range(M)]
arr.sort(key = lambda x : x[2])
for i in range(M):
    if find_parent(arr[i][0]) != find_parent(arr[i][1]):
        union(arr[i][0], arr[i][1])
        total += arr[i][2]
print(total)